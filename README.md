# My Cloud Engineering Journey 🚀

Started: April 30, 2026
Target role: Junior Cloud Engineer (Canada/US)
Daily commitment: 2-3 hours

## Week 1: Reactivation Sprint

- [x] Day 1: April 30, 2026 Environment setup complete + Linux Refresh
- [x] Day 2: May 4, 2026 Linux refresh
- [x] Day 3: Networking
- [x] Day 4: HTTP/APIs
- [x] Day 5: Git/GitHub
- [x] Day 6: Python
- [ ] Day 7: Review

## Daily Log

### Day 1 - April 30,2026

**What I learned:**

- how to install git through terminal
- how to clone git repo using terminal
- how to innstall python3 using terminal
- Linux Quick refresh:
  - linux essential commands like `pwd` `ls -la` `cd` `echo` `mkdir` and so on. Also writing on a text a file by using both `echo` and `touch` command.
  - Also, learned that using `echo` to write replaces existing text on the file. So, better use `nano` for adding contents next time.
  - system commands such as `df -h` for disk space, `free -h` to check memory usage, `ps aux` for running processes, and `history` to see all of the commands run by me/user.

**What I built:**

- Installed Gitlens on VS Code,
- installed WSL,
- Converted my MacbookAir into Linux machine
- installed Git on Linux
- Created GitHub repo for logging my daily journey

**Challenges:**

- wasn't sure git was installed properly as terminal showed some errors. Had to do quick search on google to identify the command `git --version` to check for proper installation of git.

**Tomorrow:**

- Deep dive into Linux file system structure (/home, /etc, /var, /usr)
- Practice 30 essential Linux commands with real examples
- Learn file permissions (chmod, chown) and why they matter in cloud
- Build a command cheatsheet I can reference later

### Day 2 - May 4, 2026

**What I learned:**

- `/` is the root of everything.
- `/home` is where user's work lives.
- `/etc` holds all the config files.
- `/var/log` holds the log files and caches. This is critical for debugging.
- `ls -l var/log | cat auth.log | tail -20` this gives me last 20 lines of log data on the auth.log file. It is also my first big chain command!
- The pipe was incorrect. I have to use `tail -20 /var/log/auth.log` or `cat /var/log/auth.log | tail -20`
- File Permissions:
  - `r` means Read permission. User can read the contents of the file.
  - `w` means Write persmission. User can write on the file.
  - `x` means Execute permission. User can run the file.
  - `ls -l` shows the file permissions at the start of the line.
  - `chmod` command allows changing of file permission using numbers. `r`=4, `w`=2 and `x`=1
  - First number is for `User`, second for `group` and third for `others`.
  - So the command `chmod 744 file.sh` means User has read, write and execute permission. And the group and others only have read permission.
  - This file permission system explains why I could not create a `txt` file inside `/var/log`. The owner of `/var/log` is `root` and the group is `syslog`. Everyone else has execute permission only.

**What I built:**

- Used `mkdir ~/linux-practice` to create a folder in User's home directory.
- Created three files using `touch script.sh notes.txt secret.txt`.
- Chnaged file permission of:
  - `chmod 755 script.sh`. Writeable only by me and executable by all
  - `chmod 644 notes.txt`. Writeable only by me and readable by all
  - `chmod 600 secret.txt`. Only I can read and write - like an SSH key or ENV key.
  - `ls -la` to verify the permission chnages
- Writing onto the sscript.sh file:
  - `echo '#!/bin/bash' > script.sh`. This writes the part enclosed by the quotation mark.
  - `echo 'echo Hello Cloud Engineer' >> script.sh`. This appends the `echo` command onto the file in a new line.
- Writing onto the notes.txt file:
  - `echo "These are my notes"`.
- Writing onto the secret.txt file:
  - `echo "This is private"` mimicking a secret key.
- Running the script.sh by using `bash script.sh` and it executes!.

**Challenges:**

- I could see the contents of `/var/log` from any directory I am currently in but, cannot access the content without being inside the `var/log` directory.
- So to use my previous chain command I have to run `cd /var/log` first.
- I also could not create any file inside `log` folder. Tried running `cat auth.log | tail -20 > checked-log.txt` and returned permission denied.
- Using double quote to write `echo "#!/bin/bash"` throws error: event not found. Google search revealed that any string starting with `!` causes the shell to find command in pervious history.
  -- Resolved the issue by using single quotes `''`.

**Tomorrow:**

- Learn IP addressing, CIDR notation, and the difference between public/private IPs
- Study essential ports and protocols (SSH, HTTP, HTTPS, DNS, RDP, MySQL)
- Understand how DNS resolution works and its relevance to AWS Route 53
- Practice networking commands: ping, dig, nslookup, traceroute, ss
- Build a networking cheatsheet and commit it to the repo

### Day 3 - May 5, 2026

**What I learned:**

- IP Address is a unique address that every device on a network gets. And there are public IP address and private IP address.
- Public IP is reachable over the internet and private IP is reachable only within the private network.
- CIDR notation defines range of IPs available in a network.
- DNS translates domain name into IP address for devices to connect to each other. In AWS, Route53 is the service that works as DNS service.

**What I built:**

- Checking my machines IP info
  - using command `ip addr show` and `hostname -I`
  - Both returned IP address but the the first command also gave IPv6 address as well and many other info on the NIC.

- Tested connectivity
  - Pinging google.com with command `ping google.com -c4`
  - The `-c4` flag sends 4 packets to google.com and ends the connection otherwise it pings without interruption.
  - Four packets with `icmp_seq=1` through `icmp_seq=4` was sent. Each packet was 64 bytes and with ttl=113 (ttl stands for time to liv - which defines how long the packet should live before it expires). It took about `36.5ms` to reach google.com IP `142.250.137.100`.

- DNS Lookup Tools
  - `nslookup google.com` and `dig google.com`
  - This two command queried on my local DNS resolver which then fetches information from authoritative nameservers upstream.
  - Multiple IP addresses came up on the DNS for google.com

- Checked what Ports are open on my machine
  - Used command `ss -tuln` and `netstat -tuln` to see listening ports
  - Results showed port 53 and 631 was actively listening.
  - Port 53 is used for DNS and 631 for print jobs

- Traced the route of packets to reach a server
  - Installed `traceroute`
  - Used `traceroute google.com` to trace the packets reaching to `google.com`
  - Results showed 16 hops before reaching to `google.com` server.
  - 9 hops responded while 7 hops did not.

- Checked if a specific port is open
  - Used command `nc -zv google.com 443` to check if port 443 was open on google.com. Connection succeeded and it is open.
  - Used command `nc -zv google.com 22` to check if port 22 which is used for SSH was open or not. Connection did not succeed.
  - The tool netcat's two flag used above `-z` and `-v` tells netcat tool to scan only and print the result whether succeed or not respectively.

**Challenges:**

- The command `nc -zv google.com 22` did not return anything
  - Was expecting a `"connection refused"` message as I used the `-v` verbose flag to let me know the result
  - Further research showed that if a server actively refuses then it shows `"connection refused"` and if the server does not respond to it such as port blocked/filtered then nothing happens and hanged on terminal and had to cancel manually by using `ctrl+c`.

- The missing hops on `traceroute` was configured not to respond to traceroute that I thought was skipping or ignored. It was private routers in the middle configured in that way to not to respond but do forward the packets.

**Tomorrow:**

- Day 4: HTTP/APIs

### Day 4 - May 6, 2026

**What I learned:**

- HTTP Request and Response
- HTTP Methods
  - GET - Retrieves data (Fetch a file from S3)
  - POST - Send/create data (Create an EC2 instance)
  - PUT - Update/replace data (Place a resource at a specific location you define - Upload file to S3, Create S3 bucket)
  - DELETE - Delete data (Delete an S3 object)
  - PATCH - Partial update (Update one field in a record)
- HTTP Status Codes:
  - `200` - Everything Ok
  - `201` - Resource was created successfully
  - `301` - URL has changed, redirecting
  - `400` - Request malformed
  - `401` - Not logged in or no credentials
  - `403` - Logged in but no permission
  - `404` - Resource doesn't exist
  - `500` - Server crashed
  - `502` - Load balancer got bad response from server
  - `503` - Server is overloaded or down
- API + REST

**What I Built:**

- Installed curl:
  - `sudo apt install curl -y`
  - `curl --version` to confirm

- Made API call to my github profile:
  - `curl https://api.github.com/users/ibtesam5d`
  - This returned JSON data about my profile on GitHub
  - But could not see any HTTP response or status codes just raw JSON data

- Investigated full HTTP request and response by using the `-v` flag:
  - At first the the DNS resolved at port 443 and connected
  - Second, TLS Handshake took place where the client and server agreed on the security cypher. Data showed that client (my machine) asked to change cypher. TLS handshake finished and a SSL connection was was established using TLSv1.3.
  - After the connection establishment, the request and response commenced with `HTTP 200` status code.
  - General Header, Request Header, and Response Header wass visible on the terminal along with the JSON body.

- Triggered a 404 response on purpose:
  - `curl -v https://api.github.com/users/thisuserdoesnotexist99999899898`
  - This time exact same TLS handshake happened and connection was established.
  - Get was request sent successfully
  - The response header had `HTTP 404` which is for content not found.
  - Looked at the JSON body content:
    - ```
      {
        "message": "Not Found",
        "documentation_url": "https://docs.github.com/rest",
        "status": "404"
      }
      ```
    - This JOSN revealed further information on the occured error which is content not found.

- Made a GET request and saved the output
  - Used the same command again `curl -v https://api.github.com/ibtesam5d -o ibtesam.json` but added `-o` flag for the output to save on file `ibtesam.json`.
  - verified the output by using `cat ibtesam.json`
  - Output was saved successfully

- Installed `jq` for pretty printing the JSON and saved the `"bio"` on a text file:
  - Used `sudo apt install jq -y`
  - `cat ibtesam.json | jq .` to see the full JSON
  - Accessed just one field by using `cat ibtesam.json | jq ".bio"`
  - Saved the bio on file `my_github_bio.txt` by using `cat ibtesam.json | jq ".bio" > my_github_bio.txt`
  - Verified the save using `ls` to see the file is there or not and `cat` to print the content.

**Challenges:**

- When saving the output of the GET request, only the body content was saved without any headers.
  - Used `--dump-header` flag to save the header.

**Tommorrow:**

- Learn Git branching, merging, and resolving conflicts
- Understand the GitHub workflow used in real dev teams
- Practice: create branches, make changes, merge, handle a conflict
- Build a Git cheatsheet and commit it to the repo

### Day 5 - May 8, 2026

**What I learned:**

- How Git tracks changes in three stages:
  - Working/Edit phase
  - Staging area
  - Repository (commit)

- Git workflow such as:
  - Branching,
  - merging,
  - pull requests,
  - solving merge conflicts

- Core git commands such as `git init` `git status` `git log --oneline` `git merge` `git checkout -b <branchname>` and so on.

- How branches let me work on something without breaking the main codebase.
  - I create a branch,
  - do my work and
  - if everythning checksout, I merge it to the main.

**What I Built:**

- Create and switch to a new branch
  - `git checkout -b feature/git-practice`

- Create a new file on this branch

  ```
  echo "Git Practice"> git-notes.md
  echo "Practice branching and merging">> git-notes.md
  ```

  - Stage and commit:

    ```
    git add git-notes.md
    git status #verify it's staged
    git commit -m "add git practice notes"

    ```

  - Checking the log : `git log --oneline` to see if the commit is logged
  - Switching back to main using `git checkout main`

- Merge the new feature branch to main:

  ```
  git merge feature/git-practice
  ls #to see if the .md file is now present or not
  ```

- Simulating a merge conflict:
  - Creating a file on main

    ```
    echo "Hello from main"> conflict-test.txt
    git add conflict-test.txt
    git commit -m "add conflict test file on main"

    ```

  - Creating a new branch and edit the same conflict test file:
    ```
    git checkout -b feature/conflict-test
    echo "Hello from feature branch"> conflict-test.txt
    git add conflict-test.txt
    git commit -m "edit conflict test file on feature branch"
    ```
  - Switch back to main and edit the same file again

    ```
    git checkout main
    echo "Hello from main again"> conflict-test.txt
    git add conflict-test.txt
    git commit -m "edit conflict test file on main again"
    git merge feature/conflict-test
    ```

    - This throws merge conflict error

- Resolving the merge conflict
  - Opening the conflicted file and editing to correct the issue

    ```
    cat conflict-test.txt
    <<<<<<< HEAD
    Hello from main again
    =======
    Hello from feature branch
    >>>>>>> feature/conflict-test

    nano conflict-test.txt #editing to correct the issue
    ```

  - Finally, commiting and pushing to GitHUb
    `    git add conflict-test.txt
git commit -m "resolve merge conflict"
git push origin main`

**Challenges:**

- Was confused between the command `git branch` and `git checkout -b <branchname>`
  - One creates abranch and the later creates and moved onto it
- Mistakenly created the git-cheatsheet.md file on feature branch. Merged it back to the main. But the correct response is:

  ```
  git checkout feature/git-practice -- git-cheatsheet.md

  # That file is now on main, staged and ready to commit

  git add git-cheatsheet.md
  git commit -m "bring git-cheatsheet from feature branch"
  ```

- Final checks before leaving wasdone by using `git status` and `git log --oneline`

**Tommorrow:**

- Python basics refresh — variables, loops, functions, file I/O
- Write Python scripts that do real things
- Introduction to why Python matters for cloud automation
- Build a cheatsheet and commit to repo

### Day 6 - May 12, 2026

**What I learned:**

- Why python for cloud
  - AWS automation - boto3 scripts to manage EC2, S3, IAM
  - Lambda functions - Serverless code triggered by events
  - CLI tools - Scripts that automate repetitive tasks
  - Infrastructure testing - Verify if Terraform deployed correctly
  - Log Parsing - Extract errors from CloudWatch logs

- Core Python concepts such as variables, data types, conditionals, loops, functions, file I/O

- FreeCodeCamp youtube tutorial for filling out any gaps in knowledge

**What I Built:**

- Three scripts that simulates real world AWS tasks
  - Scripts are in `cloud_scripts.py`

- Script 1: AWS Service Inventory, Simulates what boto3 returns when listing services
  - Started with a list containing AWS services

  ```
  services = [
    {"name": "EC2", "region": "ca-central-1", "running": True},
    {"name": "RDS", "region": "ca-central-1", "running": False},
    {"name": "S3", "region": "us-east-1", "running": True},
    {"name": "Lambda", "region": "ca-central-1", "running": True}
  ]
  ```

  - Looping through this `services` list for running/stopped services and printing on to the terminal console

  ```
  print("=== Running Services ===")
  for service in services:
      if service["running"]:
          print(f"{service['name']} is running in {service['region']}")

  print("\n=== Stopped Services ===")
  for service in services:
      if not service["running"]:
          print(f"{service['name']} is stopped in {service['region']} \n")
  ```

  - Result in the terminal:

  ```
  === Running Services ===
  EC2 is running in ca-central-1
  S3 is running in us-east-1
  Lambda is running in ca-central-1

  === Stopped Services ===
  RDS is stopped in ca-central-1
  ```

- Script 2: HTTP status code checker, Simulates checking response codes from AWS API calls
  - Created a function `def check_http_status(code)` that has HTTP status code mapped in a dictionary with codes and messages as key/value pair. It then returns the value given by the code. Also, added a default value `"Unknown status code"` if passed code does not match with the `status_map` dictionary

  ```
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
  ```

  - Created a list with test codes that simulates HTTP status codes from services and then looped through the list to print out the codes and messages

  ```
  test_codes = [200, 403, 404, 502, 999]

  for code in test_codes:
      print(f"{code}: {check_http_status(code)}")
  ```

  - Running the script:

  ```
  200: OK - Request successful
  403: Forbidden - Check your permissions
  404: Not Found - Resource doesn't exist
  502: Bad Gateway - Load balancer issue
  999: Unknown status code
  ```

- Script 3: Log Parser, Simulates parsing CloudWatch log entries
  - Staeted with a `logs` list that simulates logs from Cloudwatch

  ```
  logs = [
    "INFO: EC2 instance i-1234 started successfully",
    "ERROR: S3 bucket access denied for user arn:aws:iam::123",
    "INFO: Lambda function executed in 234ms",
    "ERROR: RDS connection timeout after 30s",
    "INFO: CloudWatch alarm triggered"
    ]
  ```

  - Used `open()` method to create a error log text file and writing error logs onto the file by looping through the logs and finding matching `ERROR` keyword.

  ```
  print("\n=== ERROR logs ===")
  with open("error_log.txt", "w") as f:
      for log in logs:
          if "ERROR" in log:
              print(log)
              f.write(log + "\n")


  print("\nErrors saved to error_log.txt")
  ```

  - Running the script:

  ```
  === ERROR logs ===
  ERROR: S3 bucket access denied for user arn:aws:iam::123
  ERROR: RDS connection timeout after 30s
  ```

**Challenges:**

- Ran into syntax error during `f-string` usage where I used double quotes again for the key string in the ordered list

```
print(f"{service["name"]} is stopped in {service["region"]} \n")
```

- Learned why it is highly recommended to use `with` when using `open()` method as it releases the memory automatically otherwise have to close manually to prevent memory leaking.

**Tommorrow:**

- Week 1 Review

### Day 7 -

**What I learned:**
**What I Built:**
**Challenges:**
**Tommorrow:**
