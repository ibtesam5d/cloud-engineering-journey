# Week 1 Consolidation Script
# Connects: Python + file I/O + HTTP status codes + Linux concepts

import datetime

# 1. Service inventory (from Day 6)
services = [
    {"name": "EC2", "region": "ca-central-1", "running": True, "port": 22},
    {"name": "RDS", "region": "ca-central-1", "running": False, "port": 3306},
    {"name": "S3", "region": "us-east-1", "running": True, "port": 443},
    {"name": "Lambda", "region": "ca-central-1", "running": True, "port": 443}
]

def check_http_status(code):
    status_map = {
        200 : "OK",
        403 : "Forbidden - check permissions",
        404 : "Not found",
        500 : "Server error",
        502 : "Bad gateway - load balancer issue"
    }
    return status_map.get(code, "Unknown")

# 3. Generate a report and save to file (file I/O from Day 6)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("week1_report.txt", "w") as f:
    f.write("=== Week 1 Cloud Report ===\n")
    f.write(f"Generated: {timestamp}\n\n")

    f.write("=== Running Services ===\n")
    for service in services:
        if service["running"]:
            line = f"{service['name']} | {service['region']} | port {service['port']}\n"
            print(line.strip())
            f.write(line)

    f.write("\n=== Stopped Services ===\n")
    for service in services:
        if not service["running"]:
            line = f"{service['name']} | {service['region']} | port {service['port']}\n"
            print(line.strip())
            f.write(line)
    
    f.write("\n=== HTTP Status Check ===\n")
    test_codes = [200, 403, 404, 502]
    for code in test_codes:
        line = f"{code}: {check_http_status(code)}\n"
        print(line.strip())
        f.write(line)

print("\nReport saved to week1_report.txt")

# 4. Read it back and count errors (connecting file I/O + logic)
with open("week1_report.txt", "r") as f:
    lines = f.readlines()
    error_count = sum(1 for line in lines if any(
    keyword in line.lower() for keyword in ["forbidden", "bad gateway", "error"]
))
    print(f"\nTotal issues found in report: {error_count}")