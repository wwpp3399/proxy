import mitmproxy.http
from mitmproxy import ctx, http
from httpproxy.soul.model.account import query_DeviceId_bool, upate_phone_by_smDeviceId, \
    update_login_time, query_account_info_by_phone, delete_device_by_SmDeviceId, add_deviceid_info, \
    query_now_sm_device_id_info
from httpproxy.soul.login.filter import get_phone, en_soul_id
import json
import setting
from log.log_print import logger
# from httpproxy.soul.redisdir.redis_a import redis_obj

class Counter:
    def __init__(self):
        self.num = 0
        self.get_DeviceId_conf = 'http://fp-it.fengkongcloud.com/v3/cloudconf'
        self.get_DeviceId_ios = "http://fp-it.fengkongcloud.com/v3/profile/ios"
        self.get_DeviceId_android = 'http://fp-it.fengkongcloud.com/v3/profile/android'

        self.login_url = "https://api-account.soulapp.cn/v7/account/login"
        self.refurbishToken_path = '/account/refurbishToken'

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if self.get_DeviceId_conf == flow.request.pretty_url or \
                self.get_DeviceId_android == flow.request.pretty_url or \
                self.get_DeviceId_ios == flow.request.pretty_url or \
                "soul" in flow.request.pretty_url:
            pass
        else:
            flow.response = http.HTTPResponse.make(404)
            return

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if self.get_DeviceId_android == flow.request.pretty_url or self.get_DeviceId_ios == flow.request.pretty_url:
            logger.info("-----------------------------start----------------------------------------------------------")
            logger.info("-------------------获取-feng_kong-成功------------------------------")
            get_res = flow.response.get_text()
            py_data = json.loads(get_res)
            start_smDeviceId = py_data.get("detail").get("deviceId")
            requestId = py_data.get("requestId")
            query_smDeviceId_info = query_DeviceId_bool(phoneDeviceId=start_smDeviceId)
            if query_smDeviceId_info:
                # ctx.log.info("soul-------------------数据库查到start_smDeviceId------------------------------")
                logger.info(f"-------------------数据库查到此--{start_smDeviceId}--deviceId----------------------------")
                # res_DeviceId = query_account_info_by_phone(phone=query_smDeviceId_info.get("phone")).get("smDeviceId")
                set_res_dict = {"code": 1100, "detail": {"deviceId": query_smDeviceId_info.get("nowsmdeviceid")},
                                "requestId": requestId}
                logger.info(
                    f"--------------------替换手机DeviceId为数据库中已经绑定的SM-Id---------------{query_smDeviceId_info.get('nowsmdeviceid')}")
                flow.response.set_text(json.dumps(set_res_dict, ensure_ascii=False))
            else:
                logger.info(f"--------数据库查询deviceId失败-------插入此phone登入的---{start_smDeviceId}--到数据库----------")
                add_deviceid_info(phonedeviceid=start_smDeviceId)
        if self.login_url == flow.request.pretty_url.split("?")[0]:
            logger.info(
                "soul----------------------------------------------login----------------------------------------")
            en_phone = flow.request.urlencoded_form.get("phone")
            phone = get_phone(phone=en_phone)
            sMDeviceId = flow.request.urlencoded_form.get("sMDeviceId")
            logger.info(f'--------------获取当前phone的deviceId为---------{sMDeviceId}')

            now_device_data = query_now_sm_device_id_info(nowsmdeviceid=sMDeviceId)
            if now_device_data:
                logger.info(f'--------------数据库中查到此-------{sMDeviceId}------说明第二次登录-----')
                if now_device_data.get("phone") == phone:
                    logger.info(f'-------------对比数据库中{now_device_data.get("phone")}与手机输入{phone}相同，-------------登录成功')
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
                else:
                    logger.info("-----------------------两次输phone入不一样-------------------------------")
                    delete_device_by_SmDeviceId(sMDeviceId=sMDeviceId)
                    res_login = {"code": 10002, "message": "连续两次输入号码不一致", "data": None, "success": False}
                    flow.response.set_text(json.dumps(res_login, ensure_ascii=False))
            else:
                logger.info(f'--------------数据库中没有查到-------{sMDeviceId}------说明第第一次登录-----')
                query_phone_info = query_account_info_by_phone(phone=phone)
                if query_phone_info:
                    logger.info(
                        f'--------------从account表中查取此-------{phone}--的注册SM-ID{query_phone_info.get("smDeviceId")}----进行绑定此设备的DeviceID')
                    # 返回被修改的 response
                    upate_phone_by_smDeviceId(smDeviceId=query_phone_info.get("smDeviceId"), phone=phone,
                                              deviceid=sMDeviceId)
                    res_login = {"code": 10002, "message": "账号验证成功，请大退后重启soul登录", "data": None, "success": False}
                    flow.response.set_text(json.dumps(res_login, ensure_ascii=False))

        # if self.refurbishToken_path in flow.request.pretty_url:
        #     logger.info("-------------------refurbishToken_path----------拦截成功----------")
        #     res_refurbishToken = {"code": 10001, "message": "请求成功", "data": None, "success": True}
        #     flow.response.set_text(json.dumps(res_refurbishToken, ensure_ascii=False))
