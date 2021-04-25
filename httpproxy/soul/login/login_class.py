import mitmproxy.http
from mitmproxy import ctx, http
from httpproxy.soul.model.account import query_DeviceId_bool, upate_phone_by_smDeviceId, \
    update_login_time, query_account_info_by_phone, delete_device_by_smDeviceId, add_deviceid_info,query_now_sm_device_id_info
from httpproxy.soul.login.filter import get_phone, en_soul_id
import json
import setting


class Counter:
    def __init__(self):
        self.num = 0
        self.login_path = "/v7/account/login"
        self.login_url = "https://api-account.soulapp.cn/v7/account/login"
        self.get_smDeviceId_ios = "http://fp-it.fengkongcloud.com/v3/profile/ios"
        self.get_smDeviceId_conf = 'http://fp-it.fengkongcloud.com/v3/cloudconf'
        self.get_smDeviceId_android = 'http://fp-it.fengkongcloud.com/v3/profile/android'

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.pretty_url == self.get_smDeviceId_ios or flow.request.pretty_url == self.get_smDeviceId_android \
                or flow.request.pretty_url == self.get_smDeviceId_conf or "soul" in flow.request.host:
            pass
        else:
            flow.response = http.HTTPResponse.make(404)
            return

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # ctx.log.info("soul--------------------------------------------------------------------------------")
        if flow.request.pretty_url == self.get_smDeviceId_ios or flow.request.pretty_url == self.get_smDeviceId_android:
            ctx.log.info("soul-------------------start------------------------------")
            get_res = flow.response.get_text()
            py_data = json.loads(get_res)
            start_smDeviceId = py_data.get("detail").get("deviceId")
            requestId = py_data.get("requestId")
            # ctx.log.info("启动获取start_smDeviceId---------------"+start_smDeviceId)
            # ctx.log.info("启动获取start_requestId---------------"+requestId)
            query_smDeviceId_info = query_DeviceId_bool(phoneDeviceId=start_smDeviceId)
            if query_smDeviceId_info:
                # ctx.log.info("soul-------------------数据库查到start_smDeviceId------------------------------")
                # res_DeviceId = query_account_info_by_phone(phone=query_smDeviceId_info.get("phone")).get("smDeviceId")
                set_res_dict = {"code": 1100, "detail": {"deviceId": query_smDeviceId_info.get("nowsmdeviceid")},
                                "requestId": requestId}
                # ctx.log.info(f"替换手机smDeviceId成---------------{query_smDeviceId_info.get('nowsmdeviceid')}")
                flow.response.set_text(json.dumps(set_res_dict, ensure_ascii=False))
            else:
                ctx.log.info(f"获得最新--------start_smDeviceId-------插入数据库-----{start_smDeviceId}")
                add_deviceid_info(phonedeviceid=start_smDeviceId)
        if self.login_path in flow.request.url:
            ctx.log.info("soul------------------------------------------------------------------------------------login---------------------------")
            en_phone = flow.request.urlencoded_form.get("phone")
            phone = get_phone(phone=en_phone)
            sMDeviceId = flow.request.urlencoded_form.get("sMDeviceId")
            # ctx.log.info("login获取手机号码---------------"+phone)
            # ctx.log.info("login获取MDeviceId---------------"+sMDeviceId)
            # 数据库获取与之相匹配的 phone 信息
            now_device_data = query_now_sm_device_id_info(nowsmdeviceid=sMDeviceId)
            if now_device_data:
                if now_device_data.get("phone") == phone:
                    ctx.log.info("-----------------------查询成功-------------------------------")
                    database_data = query_account_info_by_phone(phone=phone)
                    update_login_time(phone=phone)
                    delete_device_by_smDeviceId(smDeviceId=sMDeviceId)
                    with open(setting.Config.PROJECT_JSON_PATH, 'r',
                              encoding="UTF-8") as f:
                        py_login_dict = json.load(f)

                    py_login_dict["data"]["signature"] = database_data.get("nickName")
                    py_login_dict["data"]["token"] = database_data.get("token")
                    py_login_dict["data"]["userIdEcpt"] = en_soul_id(database_data.get("soulId"))
                    # 返回被修改的 response
                    flow.response.set_text(json.dumps(py_login_dict, ensure_ascii=False))
                else:

                    delete_device_by_smDeviceId(smDeviceId=sMDeviceId)
                    res_login = {"code": 10002, "message": "连续两次输入号码不一致", "data": None, "success": False}
                    flow.response.set_text(json.dumps(res_login, ensure_ascii=False))
            else:
                query_phone_info = query_account_info_by_phone(phone=phone)
                if query_phone_info:
                    ctx.log.info("----------------------更新账号信息-------------------------------")
                    ctx.log.info(query_phone_info.get("smDeviceId"))
                    # 返回被修改的 response
                    upate_phone_by_smDeviceId(smDeviceId=query_phone_info.get("smDeviceId"), phone=phone,
                                              deviceid=sMDeviceId)
                    res_login = {"code": 10002, "message": "账号验证成功，请大退后重启soul登录", "data": None, "success": False}
                    flow.response.set_text(json.dumps(res_login, ensure_ascii=False))

        # ctx.log.info("soul=========================================================================================")
