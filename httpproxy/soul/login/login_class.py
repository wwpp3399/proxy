import mitmproxy.http
from mitmproxy import ctx, http
from httpproxy.soul.model.account import query_DeviceId, upate_phone_by_smDeviceId,\
    update_login_time, query_account_info_by_phone,update_by_smDeviceId,\
    query_device_info_by,add_deviceid_info
from httpproxy.soul.login.filter import get_phone, en_soul_id
import json
import setting

class Counter:
    def __init__(self):
        self.num = 0
        self.login_url = "https://api-account.soulapp.cn/v7/account/login"
        self.get_smDeviceId_url = "http://fp-it.fengkongcloud.com/v3/profile/ios"
        self.get_smDeviceId_url_android = "http://fp-it.fengkongcloud.com/v3/profile/android"
    
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.pretty_url == self.get_smDeviceId_url_android or flow.request.pretty_url == self.get_smDeviceId_url or "soul" in flow.request.host:
            pass
        else:
            flow.response = http.HTTPResponse.make(404)
            return
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.pretty_url == self.get_smDeviceId_url or flow.request.pretty_url == self.get_smDeviceId_url_android or "soul" in flow.request.host:
            pass
        else:
            flow.response = http.HTTPResponse.make(404)
            return

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # ctx.log.info("soul--------------------------------------------------------------------------------")
        if flow.request.pretty_url == self.get_smDeviceId_url or flow.request.pretty_url == self.get_smDeviceId_url_android:
            ctx.log.info("soul-------------------start------------------------------")
            get_res = flow.response.get_text()
            py_data = json.loads(get_res)
            start_smDeviceId = py_data.get("detail").get("deviceId")
            requestId = py_data.get("requestId")
            ctx.log.info(start_smDeviceId)
            ctx.log.info(requestId)
            query_smDeviceId_info = query_DeviceId(phoneDeviceId=start_smDeviceId)
            if query_smDeviceId_info:
                ctx.log.info("soul-------------------未查到start_smDeviceId------------------------------")
                # res_DeviceId = query_account_info_by_phone(phone=query_smDeviceId_info.get("phone")).get("smDeviceId")
                set_res_dict = {"code": 1100, "detail": {"deviceId": query_smDeviceId_info.get("nowsmdeviceid")}, "requestId": requestId}
                ctx.log.info(f"找到此smID,并修改成{query_smDeviceId_info.get('nowsmdeviceid')}")
                flow.response.set_text(json.dumps(set_res_dict, ensure_ascii=False))
            else:
                add_deviceid_info(phonedeviceid=start_smDeviceId)


        if flow.request.pretty_url.split("?")[0] == self.login_url or flow.request.pretty_url == self.login_url:
            ctx.log.info("soul----------------------login---------------------------")
            en_phone = flow.request.urlencoded_form.get("phone")
            phone = get_phone(phone=en_phone)
            sMDeviceId = flow.request.urlencoded_form.get("sMDeviceId")
            ctx.log.info(phone)
            ctx.log.info(sMDeviceId)
            # 数据库获取与之相匹配的 phone 信息
            device_data = query_device_info_by(phone=phone, nowsmdeviceid=sMDeviceId)
            if device_data:
                ctx.log.info("-----------------------查询成功-------------------------------")
                database_data = query_account_info_by_phone(phone=phone)
                update_login_time(phone=phone)
                update_by_smDeviceId(smDeviceId=sMDeviceId)
                with open(setting.Config.PROJECT_JSON_PATH, 'r',
                          encoding="UTF-8") as f:
                    py_login_dict = json.load(f)

                py_login_dict["data"]["signature"] = database_data.get("nickName")
                py_login_dict["data"]["token"] = database_data.get("token")
                py_login_dict["data"]["userIdEcpt"] = en_soul_id(database_data.get("soulId"))
                # 返回被修改的 response
                flow.response.set_text(json.dumps(py_login_dict, ensure_ascii=False))

            else:
                query_phone_info = query_account_info_by_phone(phone=phone)
                if query_phone_info:
                    ctx.log.info("----------------------更新账号信息-------------------------------")
                    ctx.log.info(query_phone_info.get("smDeviceId"))
                    # 返回被修改的 response
                    upate_phone_by_smDeviceId(smDeviceId=query_phone_info.get("smDeviceId"), phone=phone,deviceid=sMDeviceId)
                    res_login = {"code": 10002, "message": "账号验证成功，请请重启soul，再次登录", "data": None, "success": False}
                    flow.response.set_text(json.dumps(res_login, ensure_ascii=False))


        # ctx.log.info("soul=========================================================================================")
