from common.qe_logging.requestLogger import RequestLogger
# from projectname.clients.base import BaseProductHelper


class ProductClient(RequestLogger):
    def __init__(self):
        super(ProductClient, self).__init__()
        self.headers = {"Content-Type": "text/xml; charset=utf-8"}

    def post_method(self, data, method, **kwargs):
        self.headers["SOAPAction"] = f'{kwargs.get("SOAPAction")}.{method}'
        return self.post(url=kwargs.get("url"), data=data, headers=self.headers)


# class ProductHelper(BaseProductHelper):
#
#     def __init__(self, client):
#         super(ProductHelper, self).__init__(client)

