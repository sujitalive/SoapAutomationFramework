from pydash import py_
from common.qe_logging import ResponseInfo
from projectname.schemas.productschema import (
    AddInteger_Schema,
    DivideInteger_Schema,
    FindPerson_Schema,
)

v1_client_path = "https://www.crcind.com:443/csp/samples/SOAP.Demo.cls"


def prep_call(
    context_call, *attributes, fixed_args=None, kwargs_from_attrs=None, **kwargs
):
    def innner(context, resp_info=None):
        attr_source = resp_info or context
        call = py_.get(context, context_call)
        args = tuple(getattr(attr_source, x, None) for x in attributes)
        if fixed_args:
            args += fixed_args
        for key in kwargs_from_attrs or []:
            kwargs[key] = getattr(attr_source, key)

        return call(*args, **kwargs)

    return innner


# REQUESTS = {
#     f"AddInteger" or f"DivideInteger" or f"FindPerson": prep_call("employee_v1_client.post_method", "data", "method"),
#     # f"AddInteger": prep_call("employee_v1_client.post_method", "data", "method"),
# }

PAYLOADREQUESTS = {
    f"AddInteger": AddInteger_Schema,
    f"DivideInteger": DivideInteger_Schema,
    f"FindPerson": FindPerson_Schema,
}


# @when("I call {request_key}")
# def step_when_call_request(context, request_key):
#     call_to_place = REQUESTS.get(request_key)
#     response_list = getattr(context, "responses", [])
#     if response_list:
#         for resp_info in context.responses:
#             resp_info.response = call_to_place(context, resp_info)
#     else:
#         context.response = call_to_place(context)


@when("I call the service")
def step_when_call_request(context):
    call_to_place = prep_call("employee_v1_client.post_method", "data", "method")
    response_list = getattr(context, "responses", [])
    if response_list:
        for resp_info in context.responses:
            resp_info.response = call_to_place(context, resp_info)
    else:
        context.response = call_to_place(context)


@given("A valid payload")
def step_given_valid_payload_for_post(context):
    context.responses.set(
        [
            ResponseInfo(
                method=row[row.headings[0]],
                data=PAYLOADREQUESTS.get(row[row.headings[0]])(
                    **remove_first_element_list(row)
                ),
            )
            for row in context.table
        ]
    )


def remove_first_element_list(row):
    row_headings = row.headings
    if row_headings[0] == "method":
        row_headings.pop(0)

    kwargs = {}
    count = 0
    for key in row_headings or []:
        count = count + 1
        kwargs[key] = row[count]

    return kwargs
