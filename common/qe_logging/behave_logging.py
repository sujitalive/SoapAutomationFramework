import logging

from common.qe_logging.config_handler import get_dictionary_from_config
from common.qe_logging.logfile_create import setup_logging

logging.getLogger("behave").setLevel(logging.DEBUG)

_all_logger = logging.getLogger("behave.all").debug
_feature_logger = logging.getLogger("behave.feature").debug
_scenario_logger = logging.getLogger("behave.scenario").debug
_step_logger = logging.getLogger("behave.step").debug

kwargs_logging = {"base_log_dir": "log", "log_name_prefix": "bahave"}


def before_all(context):
    context.environment = context.config.userdata["environment"]
    context.qe_config = get_dictionary_from_config(context.environment)
    context.tag = context.config.userdata["testtype"]
    kwargs_logging["environment"] = context.environment
    setup_logging(**kwargs_logging)


def before_feature(context, feature):
    _feature_logger("Feature: {}".format(feature.name))
    # if feature.tags:
    #     if len(feature.tags) == 1:
    #         context.tag = feature.tags[0]
    #     else:
    #         _feature_logger("        FAILED: Please provide one tag before Feature")
    #         assert context.failed is True


def before_scenario(context, scenario):
    _scenario_logger("    Scenario: {}".format(scenario.name))


def before_step(context, step):
    _step_logger("        {} {}".format(step.keyword, step.name))


def after_step(context, step):
    if step.status == "failed":
        _step_logger("        FAILED: {} {}".format(step.keyword, step.name))
        _step_logger("                {}".format(step.error_message or step.exception))
        _step_logger("--------END OF FAILURE DEBUG")
    _step_logger("")


def after_scenario(context, scenario):
    _scenario_logger("")


def after_feature(context, feature):
    _feature_logger("")


def after_all(context):
    _all_logger("")
    _all_logger("after_all - end of testing")
