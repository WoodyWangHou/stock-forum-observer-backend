from data_provider.DataProvider import DataObserver
from .RedditUtil import isValidRedditApiAP
from config.reddit_apis import HttpRequestTypeEnum, getRequests
from .AsyncJobScheduler import RecurringJob, AsyncJobScheduler
from typing import Dict, Optional
import logging

logger = logging.getLogger(__file__)


class DataSource:
    '''
        This class is an abstraction of DataSource, it represents any
        type of data source while providing abstraction for upper layer
        to subscribe to any data change
    '''

    def __init__(self, pull_interval: float) -> None:
        self._scheduler = AsyncJobScheduler()
        self._observers = []
        self._scheduler.addJob(RecurringJob(pull_interval, self.refresh))

    def registerObserver(self, observer: DataObserver) -> None:
        self._observers.append(observer)

    def refresh(self) -> None:
        for observer in self._observers:
            raw_data = self.getRawData()
            observer.update(raw_data)

    def getRawData(self) -> str:
        raise NotImplementedError(
            "Please implement getRawData method before using DataSource")


class RedditDataSource(DataSource):
    def __init__(self, access_type: HttpRequestTypeEnum, api: str, payload: Optional[Dict] = None):
        if not isValidRedditApiAP(self._api):
            raise ValueError('Received invalid api url: {}'.format(api))

        DataSource.__init(self)
        self._api = api
        self._http_request = getRequests(access_type)
        self._payload = payload

    def getRawData(self) -> str:
        if self._payload is None:
            response = self._http_request(self._api)
        else:
            response = self._http_request(self._api, self._payload)

        if not response.ok:
            logger.error(
                "Failed to get update from Reddit, access_point: {}, status code: {}".format(
                    self._api, response.status_code))
            return ""

        data = response.json()
        response.close()
        return data
