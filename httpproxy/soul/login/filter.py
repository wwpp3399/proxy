from pyDes import ECB, des, PAD_PKCS5
import base64
# import requests
import setting
import time


def get_phone(phone: str):
    b64_phone = base64.b64decode(phone.encode())
    # key_str = "789!@#xswEDCzxcv"
    py_des = des(key="789!@#xs", mode=ECB, padmode=PAD_PKCS5)
    des_de_phone = py_des.decrypt(base64.b64decode(b64_phone))
    return des_de_phone.decode()


def en_soul_id(soul_id: str):
    key = "123!@#za"
    py_des = des(key=key, mode=ECB, padmode=PAD_PKCS5)
    py_des_soul_id = py_des.encrypt(soul_id.encode())
    b64_2_soul_id = base64.b64encode(base64.b64encode(py_des_soul_id)).decode()
    return b64_2_soul_id


def de_soul_id(en_soul_id: str):
    key = "123!@#za"
    base64_soul_id = base64.b64decode(base64.b64decode(en_soul_id.encode()))
    py_des = des(key=key, mode=ECB, padmode=PAD_PKCS5)
    des_de_soul_id = py_des.decrypt(base64_soul_id)
    return des_de_soul_id.decode()


# def get_ip_port_time():
#     res = requests.get(url=setting.Config.PROXY_URL).text
#     return res + f":{int(time.time())}"
#     # list_res = res.split(":")
#     # return list_res[0], list_res[1]


def update_login_text(login_text: str):
    list_login_text = []
    return_login_text = ""
    data_list = login_text.split("&")
    for i in data_list:
        list_login_text.append(
            {i.split("=")[0]: i.split("=")[1]}
        )
    list_login_text[1]["password"] = "a215fc9adc6dce66c8b1167a0ce2f602"
    list_login_text[3]["sMDeviceId"] = "2020043015061396cb0551a34be57352714f0f73241ccd01f66cc523fdb2f7"
    for j in list_login_text:
        return_login_text += "".join(list(j.keys())[0] + "=" + list(j.values())[0]) + "&"
    # print(return_login_text[:-1])
    return return_login_text[:-1]

# update_login_text("area=86&password=a215fc9adc6dce66c8b1167a0ce2f602&phone=bjdqL0kzK0JySUw2VUUxMTJ0RW93QT09&sMDeviceId=2020043015061396cb0551a34be57352714f0f73241ccd01f66cc523fdb2f7")
