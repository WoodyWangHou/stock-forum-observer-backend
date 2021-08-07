import enum
import requests

class StringEnum(enum.Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
    
class HttpRequestTypeEnum(StringEnum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    
def getRequests(type: HttpRequestTypeEnum):
    if HttpRequestTypeEnum.GET:
        return requests.get
    elif HttpRequestTypeEnum.POST:
        return requests.post
    elif HttpRequestTypeEnum.PUT:
        return requests.put
    elif HttpRequestTypeEnum.delete:
        return requests.delete
    
    raise ValueError("Invalid Http request type: {}".format(type))
    
reddit_apis = {
    HttpRequestTypeEnum.GET: {"/r/{subreddit}/about"},
}