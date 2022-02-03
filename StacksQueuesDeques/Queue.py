class Empty(Exception):
    """Error when trying to access element from an empty container"""

    pass


class QueueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enque(self, e):
        return self._data.append(e)

    # def deque(self):
    #     # Throw error when deque on empty
    #     if len(self._data) == 0:
    #         return Empty("Cannot perform operation on empty Queue.")
    #     self._data.pop()
