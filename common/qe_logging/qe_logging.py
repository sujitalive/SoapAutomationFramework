import logging


class RequestAndResponseLogger(object):
    default_logger_name = "QE_requests"

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(self.default_logger_name)

    def log_response_status(self, response):
        self.logger.debug("-->Response status:  {}".format(response.status_code))

    def log_response_header(self, response):
        self.logger.debug("-->Response header:  {}".format(response.headers))

    def log_response_content(self, response):
        self.logger.debug(
            "-->Response content:  {}".format(response.content.decode("utf-8"))
        )

    def log_request(self, request_kwargs):
        self.logger.debug("-->client request:  {}".format(request_kwargs))

    def log_response(self, response):
        self.log_response_status(response)
        self.log_response_header(response)
        self.log_response_content(response)

    def log(self, request_kwargs, response):
        self.log_request(request_kwargs)
        self.log_response(response)
