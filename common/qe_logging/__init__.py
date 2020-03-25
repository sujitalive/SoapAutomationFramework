class ResponseInfo(object):
    def __init__(self, **kwargs):
        super(ResponseInfo, self).__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)


def list_from(item):
    if not item:
        return []
    if not is_iterable(item):
        return [item]
    return list(item)


def is_iterable(item):
    try:
        iter(item)
        return True
    except TypeError:
        return False


class ResponseList(list):
    def set(self, resp):
        self[:] = list_from(resp)
