import mitmproxy.http
from mitmproxy import ctx, http
from httpproxy.soul.model.account import query_phone_info
from httpproxy.soul.login.filter import get_phone, en_soul_id
import json
import setting


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):

        if not "soul" in flow.request.host:
            flow.response = http.HTTPResponse.make(404)
            return

    def response(self, flow: mitmproxy.http.HTTPFlow):
        url0 = "https://api-account.soulapp.cn/v7/account/login"
        ctx.log.info("soul-------------------------------------------------")
        if flow.request.pretty_url.split("?")[0] == url0 or flow.request.pretty_url == url0:
            #  根据header中os类型(ios/android) 来选择请求方式 获取request信息
            os = flow.request.headers.get("os").strip()
            data = ''
            if os.lower() == "android":
                data = flow.request.raw_content.decode()
            elif os.lower() == "ios":
                data = flow.request.get_text()
            # 分解url-header获得phone
            phone = get_phone(data)
            # 数据库获取与之相匹配的 phone 信息
            database_data = query_phone_info(phone=phone)

            if database_data:
                with open(setting.Config.PROJECT_ROOT_PATH + "/httpproxy/soul/login/login.json", 'r',
                          encoding="UTF-8") as f:
                    py_login_dict = json.load(f)

                py_login_dict["data"]["signature"] = database_data.get("nickName")
                py_login_dict["data"]["token"] = database_data.get("token")
                py_login_dict["data"]["userIdEcpt"] = en_soul_id(database_data.get("soulId"))
                # 返回被修改的 response
                flow.response.set_text(json.dumps(py_login_dict))

                ctx.log.info("soul=========================================================================")
