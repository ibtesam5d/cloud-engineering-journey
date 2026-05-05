# My Cloud Engineering Journey 🚀

Started: April 30, 2026
Target role: Junior Cloud Engineer (Canada/US)
Daily commitment: 2-3 hours

## Week 1: Reactivation Sprint

- [x] Day 1: April 30, 2026 Environment setup complete + Linux Refresh
- [x] Day 2: May 4, 2026 Linux refresh
- [ ] Day 3: Networking
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
