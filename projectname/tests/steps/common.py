from pydash import py_

v1_client_path = "http://dummy.restapiexample.com/api/v1"


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


REQUESTS = {
    f"GET {v1_client_path}/employees": prep_call("employee_v1_client.get_employees"),
    f"POST {v1_client_path}/create": prep_call("employee_v1_client.post_employee", "payload")
}


@when("I call {request_key}")
def step_when_call_request(context, request_key):
    call_to_place = REQUESTS.get(request_key)
    response_list = getattr(context, "responses", [])
    if response_list:
        for resp_info in context.responses:
            resp_info.response = call_to_place(context, resp_info)
    else:
        context.response = call_to_place(context)
