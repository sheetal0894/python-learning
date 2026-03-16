#enumerate()— Index + Value

#Normally:

services = ["nginx","redis","mysql"]

for service in services:
    print(service)

#But with index:

for index, service in enumerate(services):
    print(index, service)

#zip() — Combine Lists
servers = ["nginx","redis","mysql"]
port = [80, 6379, 3306]
for i,p in zip(servers, port):
    print (i, p)

#any() — Check if ANY True for one or more items in an iterable
services = ["nginx","redis","mysql"]
if any(s == "nginx" for s in services): #Check if nginx is running
    print("nginx is running")


#all() — Check if ALL True
services = ["nginx","redis","mysql"] 
if all(s in services for s in ["nginx","redis"]): #Check if both nginx and redis are running
    print("nginx and redis are running")