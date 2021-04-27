import mitmproxy.http
from mitmproxy import ctx
from log.log_print import logger

class LoggerCls:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        # logger.info(flow.request.url)
        # logger.info(flow.request.pretty_url)
        # logger.info(flow.request.host)
        # logger.info(flow.request.pretty_host)
        # logger.info(flow.request.path)
        # logger.info(flow.request.query)
        # ctx.log.info("We've seen %d flows" % self.num)