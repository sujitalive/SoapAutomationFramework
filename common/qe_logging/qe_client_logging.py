import requests
import logging

from common.qe_logging.qe_logging import RequestAndResponseLogger


class RequestsLoggingClient(requests.Session):
    _logger = logging.getLogger(__name__)

    def __init__(
        self,
        base_url=None,
        curl_logger=None,
        accept="application/json",
        content_type="application/json",
        response_formatter=False,
        response_retry_checker=False,
    ):
        self.default_header = {"Accept": accept, "Content-Type": content_type}
        self.base_url = base_url
        self.curl_logger = self._initialized_logger(
            curl_logger or RequestAndResponseLogger
        )
        self.response_formatter = response_formatter
        self.response_retry_checker = response_retry_checker
        kwargs = {}
        super(RequestsLoggingClient, self).__init__(**kwargs)

    def _initialized_logger(self, curl_logger):
        return (
            curl_logger(self._logger) if isinstance(curl_logger, type) else curl_logger
        )

    def request(
        self, method, url, curl_logger=None, response_retry_checker=None, **kwargs
    ):
        response_retry_checker = response_retry_checker or self.response_retry_checker
        kwargs["headers"] = dict(self.default_header, **(kwargs.get("headers", {})))
        # full_url = f"{self.base_url}{url}"
        full_url = url
        request_kwargs = {"method": method, "url": url, "kwargs": kwargs}
        response = self._make_actual_request(
            method, full_url, curl_logger, request_kwargs
        )
        return response

    def _make_actual_request(self, method, full_url, curl_logger, request_kwargs):
        try:
            response = super(RequestsLoggingClient, self).request(
                method, full_url, verify=False, **request_kwargs["kwargs"]
            )
        except Exception:
            self._get_logger(self, curl_logger)
            raise

        self._get_logger(curl_logger).log(request_kwargs, response)
        return response

    def _get_logger(self, curl_logger):
        if curl_logger:
            return self._initialized_logger(curl_logger)
        return self.curl_logger
