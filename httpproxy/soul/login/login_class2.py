import mitmproxy.http
from mitmproxy import ctx, http
from httpproxy.soul.model.account import update_login_time, query_account_info_by_phone

from httpproxy.soul.login.filter import get_phone, en_soul_id
import json
import setting
from log.log_print import logger


class Counter:
    def __init__(self):
        self.num = 0
        self.login_url = "https://api-account.soulapp.cn/v7/account/login"

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "soul" in flow.request.pretty_url:
            pass
        else:
            flow.response = http.HTTPResponse.make(404)
            return

    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("--------------------------------------------------")
        if self.login_url == flow.request.pretty_url.split("?")[0]:
            logger.info(
                "soul----------------------------------------------login----------------------------------------")
            en_phone = flow.request.urlencoded_form.get("phone")
            phone = get_phone(phone=en_phone)
            sMDeviceId = flow.request.urlencoded_form.get("sMDeviceId")
            logger.info(f'--------------获取当前phone的deviceId为---------{sMDeviceId}')

            database_data = query_account_info_by_phone(phone=phone)
            update_login_time(phone=phone)
            logger.info(f'-------------更新此{phone}的第一次登录时间---------------------------')
            # delete_device_by_smDeviceId(smDeviceId=sMDeviceId)
            with open(setting.Config.PROJECT_JSON_PATH, 'r',
                      encoding="UTF-8") as f:
                py_login_dict = json.load(f)

            py_login_dict["data"]["signature"] = database_data.get("nickName")
            py_login_dict["data"]["token"] = database_data.get("token")
            py_login_dict["data"]["userIdEcpt"] = en_soul_id(database_data.get("soulId"))
            # 返回被修改的 response
            flow.response.set_text(json.dumps(py_login_dict, ensure_ascii=False))


