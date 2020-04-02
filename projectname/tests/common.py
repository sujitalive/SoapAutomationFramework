import os
from datetime import datetime
import xml.dom.minidom


def createOutputXmls(context, resp_info):
    environment_name = getattr(context, "environment")
    base_log_dir = getattr(context, "tag")
    master_logfile_prefix = getattr(resp_info, "scenarioname")
    method_name = getattr(resp_info, "method")

    timestamp = "{:%Y%m%d}".format(datetime.now())
    timestamp_log_dir = os.path.join(*(base_log_dir,) + (environment_name,) + (timestamp,) + (method_name,))
    master_logfile_name = "{}.xml".format(master_logfile_prefix.lower())

    for dir_ in [timestamp_log_dir]:
        if not os.path.exists(dir_):
            os.makedirs(dir_)

        log_filename = os.path.join(dir_, master_logfile_name)
        f = open(log_filename, "w", encoding="UTF-8")
        xmlParse = xml.dom.minidom.parseString(resp_info.response.content)
        xml_pretty_str = xmlParse.toprettyxml()

        f.write(xml_pretty_str)
        f.close()
