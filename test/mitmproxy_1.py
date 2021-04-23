import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        # 忽略非百度搜索地址
        if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
            return

        # 确认请求参数中有搜索词
        if "wd" not in flow.request.query.keys():
            ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
            return

        # 输出原始的搜索词
        ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        # 替换搜索词为“360搜索”
        flow.request.query.set_all("wd", ["360搜索"])

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 忽略非 360 搜索地址
        if flow.request.host != "www.so.com":
            return

        # 将响应中所有“搜索”替换为“请使用谷歌”
        text = flow.response.get_text()
        text = text.replace("搜索", "请使用谷歌")
        flow.response.set_text(text)

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        # 确认客户端是想访问 www.google.com
        if flow.request.host == "www.google.com":
            # 返回一个非 2xx 响应断开连接
            flow.response = mitmproxy.http.HTTPResponse.make(404)
addons = [
    Counter()
]