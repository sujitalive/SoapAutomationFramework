from common.qe_logging.requestLogger import RequestLogger
from projectname.clients.base import BaseProductHelper
from projectname.schemas.productschema import CREATE_EMPLOYEE_PAYLOAD, AddInteger_Schema


class ProductClient(RequestLogger):
    def __init__(self):
        super(ProductClient, self).__init__()
        self.url = f"https://www.crcind.com:443/csp/samples/SOAP.Demo.cls"
        self.SOAPAction = "http://tempuri.org/SOAP.Demo"
        self.headers = {"Content-Type": "text/xml; charset=utf-8"}

    def post_method(self, data, method):
        self.headers["SOAPAction"] = f"{self.SOAPAction}.{method}"
        return self.post(self.url, data=data, headers=self.headers)


# class ProductHelper(BaseProductHelper):
#
#     def __init__(self, client):
#         super(ProductHelper, self).__init__(client)
#         self.payloadinitialiser = wrapper_payload
#
#     def employee_payload(self):
#         return self.payloadinitialiser()
