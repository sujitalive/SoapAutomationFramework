from common.qe_logging import ResponseInfo
from projectname.schemas.productschema import CREATE_EMPLOYEE_PAYLOAD


@then("The response should be OK")
def step_then_response_status(context):
    context.responses.set(ResponseInfo(test1="sujit"))
    response_list = getattr(context, "responses", [])
    if response_list:
        for resp_info in context.responses:
            x = resp_info.test1
    print("Then The response should be OK")


@given("A valid payload to create an employee")
def step_given_valid_payload_to_create_employee(context):
    UPDATE_EMPLOYEE_PAYLOAD_FIELDS = {"name":"newSujit", "age":"33"}
    payload = context.payloadcreator(CREATE_EMPLOYEE_PAYLOAD, UPDATE_EMPLOYEE_PAYLOAD_FIELDS)
    context.responses.set(ResponseInfo(payload=payload))
