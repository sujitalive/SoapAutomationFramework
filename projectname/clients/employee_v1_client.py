from common.qe_logging.requestLogger import RequestLogger
from projectname.clients.base import BaseProductHelper
from projectname.schemas.productschema import wrapper_payload, CREATE_EMPLOYEE_PAYLOAD


class ProductClient(RequestLogger):
    def __init__(self):
        super(ProductClient, self).__init__()

    @property
    def employee_api_path(self):
        return f"http://dummy.restapiexample.com/api/v1"

    def get_employees(self):
        return self.get(f"{self.employee_api_path}/employees")

    def get_employee(self, employee_id):
        return self.get(f"{self.employee_api_path}/employee/{employee_id}")

    def post_employee(self, payload=None):
        return self.post(f"{self.employee_api_path}/create", json=payload)

    def put_employee(self, employee_id, payload=None):
        return self.put(f"{self.employee_api_path}/update/{employee_id}", json=payload)

    def delete_employee(self, employee_id, payload=None):
        return self.delete(
            f"{self.employee_api_path}/delete/{employee_id}", json=payload
        )


class ProductHelper(BaseProductHelper):

    def __init__(self, client):
        super(ProductHelper, self).__init__(client)
        self.payloadinitialiser = wrapper_payload

    def employee_payload(self):
        return self.payloadinitialiser()

