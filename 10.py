class IterExample(Iter):
    def __init__(self, collection, cursor):
        super().__init__(collection, cursor)

    def first(self):
        self._cursor = -1

    def next(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        return self._collection[self._cursor]