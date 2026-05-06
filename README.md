# My Cloud Engineering Journey 🚀

Started: April 30, 2026
Target role: Junior Cloud Engineer (Canada/US)
Daily commitment: 2-3 hours

## Week 1: Reactivation Sprint

- [x] Day 1: April 30, 2026 Environment setup complete + Linux Refresh
- [x] Day 2: May 4, 2026 Linux refresh
- [x] Day 3: Networking
- [ ] Day 4: HTTP/APIs
- [ ] Day 5: Git/GitHub
- [ ] Day 6: Python
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
