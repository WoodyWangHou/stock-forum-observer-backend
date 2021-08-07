from urllib.parse import urlparse


def isValidRedditApiAP(access_point: str) -> bool:
    parseResult = urlparse(access_point)

    if parseResult.scheme != "https":
        return False

    if parseResult.netloc != "api.reddit.com":
        return False
