import abc


class QueryObject(object):

    filter = None

    @abc.abstractmethod
    def query(self, *args, **kwargs):
        pass

    def __init__(self, request, *args, **kwargs):
        self.request = request
        if self.filter:
            self.filter = self.filter(request)

    def run(self, *args, **kwargs):
        query = self.query(*args, **kwargs)
        if self.filter:
            query = self.filter.apply(query)
        return query.all()
