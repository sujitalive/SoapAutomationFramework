import os
from datetime import datetime
import logging

DEFAULT_FORMATTER_STRING = "%(asctime)s:%(levelname)-8s:%(name)-25s:%(message)s"


def setup_logging(**kwargs):
    base_log_dir = kwargs.get("base_log_dir")
    master_logfile_prefix = kwargs.get("log_name_prefix")

    result = []
    root_log = logging.getLogger("")
    formatter = logging.Formatter(DEFAULT_FORMATTER_STRING)

    if any(isinstance(x, logging.FileHandler) for x in root_log.handlers):
        return result

    timestamp = "{:%Y%m%d_%H%M%S}".format(datetime.now())
    timestamp_log_dir = os.path.join(*(base_log_dir,) + (timestamp,))
    master_logfile_name = "{}.master.log".format(master_logfile_prefix.lower())

    for dir_ in (timestamp_log_dir, base_log_dir):
        if not os.path.exists(dir_):
            os.makedirs(dir_)

        log_filename = os.path.join(dir_, master_logfile_name)
        result.append(log_filename)

        log_handler = logging.FileHandler(log_filename, mode="w", encoding="UTF-8")
        log_handler.setFormatter(formatter)
        root_log.addHandler(log_handler)

    return result
