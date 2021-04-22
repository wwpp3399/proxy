import redis
import time
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
redis_obj = redis.Redis(connection_pool=pool)


# redis_obj.set("hucheng",value="我爱你",ex=5)
# for i in range(0,6):
#     print("---")
#     time.sleep(1)
# print(redis_obj.get("hucheng"))

# redis_obj.set(name="hucheng",value="欧尼酱")
# print(redis_obj.keys())
# print(redis_obj)
# time.sleep(1)
# print(redis_obj.get("hucheng"))

for i in redis_obj.keys():
    # redis_obj.delete(i)
    print(i)
# redis_obj.delete("29y0jtJf")
# print(redis_obj.get(name="29y0jtJf"))


