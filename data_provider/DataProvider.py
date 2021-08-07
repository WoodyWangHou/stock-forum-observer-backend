
class DataObserver:
    def update(self):
        pass

class DataProvider(DataObserver):
    def parse(self, raw_data: str):
        raise NotImplementedError("Please implement Data Provider")

    def getData(self):
        raise NotImplementedError("Please implement Data Provider")
    
    
class RedditDataProvider(DataProvider):
    def 
