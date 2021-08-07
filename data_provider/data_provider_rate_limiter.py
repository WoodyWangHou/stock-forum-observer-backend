
class DataProviderRateLimiter:
    def get_rate(self) -> int:
        pass
    
    
class RedditDataProviderRateLimiter:
    # The rate limit is 60 requests per minute
    # Details: https://github.com/reddit-archive/reddit/wiki/API
    REDDIT_RATE_LIMIT = 60
    def __init__(self):
        self._rate