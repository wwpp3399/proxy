import os


class Config:
    PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    PROJECT_JSON_PATH = os.path.join(PROJECT_ROOT_PATH, "httpproxy", "soul", "login", "login.json")
    # PROXY_URL = "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=0&city=0&yys=0&port=11&time=3&ts=0&ys=0&cs=0&lb=4&sb=0&pb=45&mr=1&regions=440000&gm=4"

# print(Config.PROJECT_JSON_PATH)
