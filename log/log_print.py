import logging
from setting import Config
import os

# 定义 logger 对象来记录日志
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# 设置logging 格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 定义文件输出日志 处理器
lf_handler = logging.FileHandler(os.path.join(Config.PROJECT_ROOT_PATH, "log", "login.log"),mode='w',encoding='UTF-8')
lf_handler.setLevel(logging.INFO)
lf_handler.setFormatter(formatter)

# 定义console输出日志 处理器
lc_handler = logging.StreamHandler()
lc_handler.setLevel(logging.WARNING)
lc_handler.setFormatter(formatter)


# 绑定
logger.addHandler(lf_handler)
logger.addHandler(lc_handler)
