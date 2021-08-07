
import asyncio
from typing import Optional, Callable


class AsyncJob:
    '''
        This is the basic abstraction of a asynchronous job that will be
        scheduled for io, network call
    '''

    def __init__(self, func: Callable[[], None]) -> None:
        self._func = func

    async def execute(self) -> None:
        self._func()


class RecurringJob(AsyncJob):
    '''
        RecurringJob is a type of AsyncJob that will be invoked repeatedly for a given interval
    '''

    def __init__(self, interval_secs: Optional[float], func: Callable[[], None]) -> None:
        AsyncJob.__init(self, func)
        if interval_secs is not None:
            self._interval = interval_secs

    async def execute(self) -> None:
        while(True):
            await AsyncJob.execute()
            if self._interval is not None:
                await asyncio.sleep(self._interval)


class AsyncJobScheduler:
    def __init__(self):
        self._jobs = []
        self._event_loop = asyncio.get_event_loop()

    def addJob(self, job: AsyncJob) -> None:
        self._jobs.append(job)
        self._even_loop.create_task(job.execute())

    def run(self) -> None:
        try:
            self._even_loop.run_forever()
        finally:
            self._even_loop.run_until_complete(
                self._even_loop.shutdown_asyncgens())
            self._even_loop.close()
