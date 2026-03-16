# # import json

# # server = {
# #  "name": "nginx",
# #  "cpu": 70
# # }

# # with open("server.json","w") as file:
# #     json.dump(server,file)


# # import json

# # data = '''
# # [
# #  {"name":"nginx","cpu":50},
# #  {"name":"redis","cpu":90}
# # ]
# # '''

# # servers = json.loads(data)
# # print(data)
# # print (servers)
# # for s in servers:
# #     print(s["name"], s["cpu"])


# # import json

# # response = '{"status":"success","data":{"pod":"nginx","cpu":75}}'

# # data = json.loads(response)

# # print(data["data"]["pod"])





# import json

# server = {"name":"nginx","cpu":70}

# print(json.dumps(server, indent=2))
# print(json.dumps(server))


# server_1 = {
#  "name":"nginx",
#  "cpu":70
# }

# jsonfile=json.dumps(server_1)
# print(jsonfile)

# jsonkey='{"service":"redis","status":"running"}'
# s=json.loads(jsonkey)
# print (s["service"])

# json_list = '''[
#  {"name":"nginx","cpu":40},
#  {"name":"redis","cpu":90}
# ]'''

# servers_2 = json.loads(json_list)
# for s in servers_2:
#     print(s["name"], s["cpu"])



# import json

# server = {
#     "name": "nginx",
#     "cpu": 700
# }

# with open("server.json", "w") as file:
#     json.dump(server, file)

# print("JSON file created")
