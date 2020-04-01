from projectname.tests.common import createOutputXmls

RESPONSE_CODE = {"OK": 200}


@then("The response should be {request_key}")
def step_then_response_status(context, request_key):
    response_list = getattr(context, "responses", [])
    if response_list:
        for resp_info in context.responses:
            if resp_info.response.status_code != RESPONSE_CODE.get(
                str(request_key).upper()
            ):
                assert context.failed is True
                context.error_message = "not found"
            else:
                if getattr(context, "tag", []):
                    if getattr(context, "tag") == "beforedeployement" or "afterdeployement":
                        createOutputXmls(context, resp_info)
