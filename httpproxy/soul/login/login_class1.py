# # import mitmproxy.http
# # from mitmproxy import ctx, http
# from httpproxy.soul.model.account import query_phone_info
# from httpproxy.soul.login.filter import get_phone, en_soul_id, get_ip_port_time, update_login_text, de_soul_id
# import json
# import setting
# from httpproxy.soul.redisdir.redis_a import redis_obj
# import time


# class Counter:
#     def __init__(self):
#         self.num = 0
#
#     def request(self, flow: mitmproxy.http.HTTPFlow):
        # return
        # global port, ip
        # global ip, port
        # if flow.request.method == "CONNECT":
        #     return
        # return
        # # if not "soul" in flow.request.host:
        # #     flow.response = http.HTTPResponse.make(404)
        #
        # ctx.log.info("soul-------------------------------------------------")
        # if True:
        #     ip = "113.103.136.197"
        #     port = 4256
        # ip, port = None, None
        #
        # login_text = flow.request.text
        #
        # flow.request.text = update_login_text(login_text)
        #
        # ctx.log.info(flow.request.text)
        # flow.request.urlencoded_form["osv"] = osv
        # ctx.log.info(flow.request.get_text())
        # flow.request.headers["x-auth-userid"]

        #
        # ctx.log.info("soul22222222222222222222222222222222222222222222222222222222")
        # user_id = flow.request.headers.get("x-auth-userid")
        # ctx.log.info(f"++++redis_obj.keys为----{redis_obj.keys()}333333333333333333333333333333333333333333333333333333")
        # if user_id in redis_obj.keys():
        #     ctx.log.info(
        #         f"++++soul的ID为----{user_id}------444444444444444444444444444444444444444444444444444444444")
        #     r_ip_port_time = redis_obj.get(user_id)
        #     if int(time.time()) < int(r_ip_port_time.split(":")[2])+60*2:
        #         ctx.log.info(f"已有ip,分拆ip_port{r_ip_port_time},")
        #         ip = r_ip_port_time.split(":")[0]
        #         port = int(r_ip_port_time.split(":")[1])
        #     else:
        #         ip_port_time = get_ip_port_time()
        #         ctx.log.info(f"创建ip_port{ip_port_time},")
        #         redis_obj.set(name=user_id, value=ip_port_time, xx=True)
        #         ip = ip_port_time.split(":")[0]
        #         port = int(ip_port_time.split(":")[1])
        # if flow.request.method == "CONNECT":
        #     # If the decision is done by domain, one could also modify the server address here.
        #     # We do it after CONNECT here to have the request data available as well.
        #     return
        #     client_ip = flow.client_conn.address[0]
        #     if 'soul' in flow.request.host:
        #         ctx.log.info(flow.request.url)
        #         proxy = ("localhost", 8888)
        #     else:
        #         proxy = ("localhost", 3800)
        # proxy = ("113.75.148.132", 4265)
        # if flow.live:
            # ctx.log.info(f"{ip}++++{str(port)}+++++++++{type((ip,port))}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    #     flow.live.change_upstream_proxy_server(("27.44.216.73", 4213))
    #
    # # return
    #
    # def response(self, flow: mitmproxy.http.HTTPFlow):
    # #     ctx.log.info(flow.response.text)
    #     return
        # url0 = "https://api-account.soulapp.cn/v7/account/login"
        #
        # if flow.request.pretty_url.split("?")[0] == url0 or flow.request.pretty_url == url0:
        #     ctx.log.info("soul-----------------response--------------------------------")
        #     ctx.log.info(flow.response.text)
        #     en_soul_id = json.loads(flow.response.text).get("data").get("userIdEcpt")
        #     soul_id = de_soul_id(en_soul_id)
        # ip_port = get_ip_port()
        # ctx.log.info(f"创建ip_port{ip_port},")
        # redis_obj.set(name=user_id, value=ip_port, ex=60)
        # ip = ip_port.split(":")[0]
        # port = ip_port.split(":")[1]
        # ctx.log.info(flow.response.text)
        #  根据header中os类型(ios/android) 来选择请求方式 获取request信息
        # os = flow.request.headers.get("os").strip()
        # data = ''
        # if os.lower() == "android":
        #     data = flow.request.raw_content.decode()
        # elif os.lower() == "ios":
        #     data = flow.request.get_text()
        # # 分解url-header获得phone
        # phone = get_phone(data)
        # # 数据库获取与之相匹配的 phone 信息
        # database_data = query_phone_info(phone=phone)
        # # ctx.log.info(database_data)
        # if database_data:
        #     with open(setting.Config.PROJECT_ROOT_PATH + "/httpproxy/soul/login/login.json", 'r',
        #               encoding="UTF-8") as f:
        #         py_login_dict = json.load(f)
        #
        #     py_login_dict["data"]["signature"] = database_data.get("nickName")
        #     py_login_dict["data"]["token"] = database_data.get("token")
        #     py_login_dict["data"]["userIdEcpt"] = en_soul_id(database_data.get("soulId"))

        # ip_port_time = get_ip_port_time()
        # redis_obj.set(name=soul_id, value=ip_port_time)
        # # 返回被修改的 response
        #
        # flow.response.set_text(json.dumps(py_login_dict))
        #
        # ctx.log.info(f"soul======{soul_id}+++++{ip_port_time}===================================================================")

        # if flow.live:
        #     # ctx.log.info(f"{ip}++++{str(port)}+++++++++{type((ip,port))}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #
        #     flow.live.change_upstream_proxy_server(proxy)

