from pydash import py_
from common.qe_logging import ResponseInfo
from projectname.schemas.productschema import (
    AddInteger_Schema,
    DivideInteger_Schema,
    FindPerson_Schema,
)


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


PAYLOADREQUESTS = {
    f"AddInteger": AddInteger_Schema,
    f"DivideInteger": DivideInteger_Schema,
    f"FindPerson": FindPerson_Schema,
}


@when("I call the service")
def step_when_call_request(context):
    kwargs = {
        "url": context.qe_config.get("url"),
        "SOAPAction": context.qe_config.get("SOAPAction"),
    }
    call_to_place = prep_call(
        "employee_v1_client.post_method", "data", "method", **kwargs
    )
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
                scenarioname=row[row.headings[0]],
                method=row[row.headings[1]],
                data=PAYLOADREQUESTS.get(row[row.headings[1]])(
                    **generate_dictionary_from_row(row)
                ),
            )
            for row in context.table
        ]
    )


def generate_dictionary_from_row(row):
    kwargs = {}
    for key, value in zip(row.headings, row):
        kwargs[key] = value
    return kwargs
