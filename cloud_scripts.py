#script 1: AWS service inventory
#Simulates what boto3 returns when listing services

services = [
    {"name": "EC2", "region": "ca-central-1", "running": True},
    {"name": "RDS", "region": "ca-central-1", "running": False},
    {"name": "S3", "region": "us-east-1", "running": True},
    {"name": "Lambda", "region": "ca-central-1", "running": True}
]

print("=== Running Services ===")
for service in services:
    if service["running"]:
        print(f"{service['name']} is running in {service['region']}")

print("\n=== Stopped Services ===")
for service in services:
    if not service["running"]:
        print(f"{service['name']} is stopped in {service['region']} \n")


#Script 2: HTTP status code checker
#Simulates checking response codes from AWS API calls

def check_http_status(code):
    status_map = {
        200: "OK - Request successful",
        201: "Created - Resource created",
        400: "Bad Request - Check your input",
        401: "Unauthorized - Check your credentials",
        403: "Forbidden - Check your permissions",
        404: "Not Found - Resource doesn't exist",
        500: "Internal Server Error - Server side issue",
        502: "Bad Gateway - Load balancer issue"
    }
    return status_map.get(code, "Unknown status code")


test_codes = [200, 403, 404, 502, 999]

for code in test_codes:
    print(f"{code}: {check_http_status(code)}")


#Script 3: Log Parser
#Simulates parsing CloudWatch log entries

logs = [
    "INFO: EC2 instance i-1234 started successfully",
    "ERROR: S3 bucket access denied for user arn:aws:iam::123",
    "INFO: Lambda function executed in 234ms",
    "ERROR: RDS connection timeout after 30s",
    "INFO: CloudWatch alarm triggered"
    ]

print("\n=== ERROR logs ===")
with open("error_log.txt", "w") as f:
    for log in logs:
        if "ERROR" in log:
            print(log)
            f.write(log + "\n")


print("\nErrors saved to error_log.txt")