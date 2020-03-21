import logging

from common.qe_logging.qe_client_logging import RequestsLoggingClient


class RequestLogger(RequestsLoggingClient):

    _logger = logging.getLogger(__name__)

    def __init__(self):
        self._logger.setLevel(logging.DEBUG)
        super(RequestLogger, self).__init__()

    def log(self, data):
        logging.basicConfig(level=logging.DEBUG)
        self._logger.debug(data)
