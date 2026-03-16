# def green(name):
#    # print (f"\033[92m{name}\033[0m")
#    print(name)

# green("this is green text")


# def check(port):
#     if port==80:
#         print("web server is running")
#     else:
#         print("web server is not running")

# check(90)

# def is_high_cpu(cpu):
#   if cpu > 80:
#     print("High CPU usage")


# is_high_cpu(85)


servers = [
 {"name":"nginx","cpu":50},
 {"name":"redis","cpu":90},
 {"name":"mysql","cpu":60}
]

def check_server(s):
        if s["cpu"] > 80:
            print ( s["name"] ,"is running with high CPU usage:", s["cpu"])
            print(f"{s['name']} is printing using f string {s['cpu']}")
            print("{} is printing using format method {}".format(s["name"], s["cpu"]))

for s in servers:
    check_server(s)