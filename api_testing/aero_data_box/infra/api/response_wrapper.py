class ResponseWrapper:
    def __init__(self, ok, status, data):
        self._ok = ok
        self._status = status
        self._data = data