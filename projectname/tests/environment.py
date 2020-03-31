from common.qe_logging import behave_logging, ResponseList
from projectname.clients.employee_v1_client import ProductClient


def before_all(context):
    import ipdb

    ipdb.set_trace()
    context.employee_v1_client = ProductClient()
    # context.employee_v1_helper = ProductHelper(context.employee_v1_client)
    behave_logging.before_all(context)
    # context.url = context.qe_config.get("url")
    # context.SOAPAction = context.qe_config.get("SOAPAction")
    context.responses = ResponseList()
    # context.payloadcreator = (context.employee_v1_helper.employee_payload())


def after_all(context):
    behave_logging.after_all(context)


def before_feature(context, feature):
    behave_logging.before_feature(context, feature)


def after_feature(context, feature):
    behave_logging.after_feature(context, feature)


def before_scenario(context, scenario):
    behave_logging.before_scenario(context, scenario)
    context.responses.clear()


def after_scenario(context, scenario):
    behave_logging.after_scenario(context, scenario)
    context.responses.clear()


def before_step(context, step):
    behave_logging.before_step(context, step)


def after_step(context, step):
    behave_logging.after_step(context, step)
