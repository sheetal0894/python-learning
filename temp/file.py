# file = open("logs.txt","r")

# data = file.read()

# print(data)

# file.close()



# with open("logs.txt","r") as file:
#     data = file.read()
#     print(data)


# with open("logs.txt","r") as file:
    
#     for line in file:
#         print(line)

# with open("output.txt","w") as file:
#     file.write("This is a new file created using Python.\n")
#     file.write("It contains some sample text data.\n")
#     file.write("This is the third line of the file.\n")

# with open("output.txt","a") as file:
#     file.write("This is a new file created using Python append .\n")
#     file.write("It contains some sample text data append.\n")
#     file.write("This is the third line of the file append.\n")


#     logs = [
# "nginx started",
# "redis started",
# "mysql started"
# ]
    
# with open("writefile.txt","w") as file:
#     for logs in logs:
#         file.write(logs + "\n  ")



import json

# with open("server.json","r") as file:

#     data = json.load(file)

# print(data)

# print ("server.json")


# with open("services.txt","r" )as file:
#           for line in file:
#                print(line.strip())
    
    #readlines() method reads all lines and returns a list of lines
with open("writefile.txt","r") as file:
    for line in file:
        if "ERROR" in line:
           print(line.strip())

        #strip() method removes leading and trailing whitespace characters from a string, including the newline character (\n) at the end of each line. This is useful when reading lines from a file, as it helps to clean up the output by removing unnecessary whitespace.
# with open
# with open("server.json","r") as file:
#         data= json.loads(file.read())
#         for s in data:
#                 print(f"server {s['Server']} cpu {s['CPU']}")

