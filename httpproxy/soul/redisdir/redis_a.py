import redis
import time
pool = redis.ConnectionPool(host='39.103.174.179', port=6389, decode_responses=True)
redis_obj = redis.Redis(connection_pool=pool)

pool = redis.ConnectionPool(host='39.103.174.179', port=6399, decode_responses=True)
redis_obj2 = redis.Redis(connection_pool=pool)



# redis_obj.hset('p_info', 'hucheng', '27')
# redis_obj.hset('p_info', 'xiaoming', {"phonedid":"12321","nowsmid":"21312","phone":"311231"})

# print(redis_obj.hmget("p_info", ["hucheng","xuesong","xiaoming"]))
# redis_obj.set("hucheng01",value={"a":"1231","b":"234234"})
# # redis_obj.set(name="hucheng",value="欧尼酱")
# # print(redis_obj.keys())
# # print(redis_obj)
# # time.sleep(1)
# # print(redis_obj.get("hucheng"))
#
# for i in redis_obj.keys():
#     # redis_obj.delete(i)
#     print(i)
#
# for i in redis_obj2.keys():
#     # redis_obj.delete(i)
#     print(i)
# print(redis_obj.keys())
# redis_obj.delete("29y0jtJf")
# print(redis_obj.get(name="29y0jtJf"))
# print(redis_obj.mset(mapping={"http":"12321","https":"123123"}))
# redis_obj2.set(name="hucheng",value="fsadfsafasf")
# print(redis_obj.get("20210422225648e02c4f194eeee087b7adc2285bc6d35a01fc31dc6bc9f281"))
# print(redis_obj2.get("hucheng"))
# print(redis_obj.get("hucheng01"))
# for i in redis_obj.keys():
#     print(i)
# redis_obj.hmset("hucheng",{"nowsmdeviceid": '', "phone": ''})
# print(redis_obj.hexists("hucheng1"))
# print(redis_obj.hgetall("hucheng"))
# redis_obj.delete("hucheng")