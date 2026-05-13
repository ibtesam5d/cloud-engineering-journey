#strings

name = "cloud-engineer"
region = "ca-central-1"

#numbers
port = 443
cost = 0.023

#boolean
is_running = True
is_public = False

#Lists
services = ["EC2","S3","RDS", "Lambda"]

#Dictionaries
instance = {
    "id" : "i-1234abcd",
    "type" : "t2-micro",
    "region" : "ca-central-1",
    "running" : True
}

#conditionals
status_code = 200

if status_code == 200:
    print("Success")
elif status_code == 404:
    print("Not Found")
else:
    print("Something Went Wrong")

#looping through a list
for service in services:
    print(f"AWS Service: {service}")


for i in range(5,10):
    print(f"The number: {i}")


#Functions
def check_status(code):
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    else:
        return "Error"

result = check_status(status_code)
print(result)

#File I/O
#Write some logs
with open("server.log", "w") as f:
    f.write("INFO: Server Started\n")
    f.write("ERROR: Connection timeout\n")
    f.write("INFO: Request Completed\n")

#Read the logs and filter only errors
with open("server.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

#Reading the full log
with open("server.log", "r") as f:
    content = f.read()
    print(content)


ec2_services = [
    {"name": "EC2", "region": "ca-central-1", "running": True},
    {"name": "EC2", "region": "ca-central-2", "running": False},
    {"name": "EC2", "region": "ca-east-1", "running": True},
    {"name": "EC2", "region": "ca-west-1", "running": False},
]

for service in ec2_services:
    if not service['running']:
        print(f"The EC2 in region {service['region']} is stopped")


# Causes syntax error — Python gets confused by nested double quotes
print(f"{service["name"]}")

# Fix 1: use single quotes for the key inside f-string
print(f"{service['name']}")

# Fix 2: store in variable first
name = service["name"]
print(f"{name}")