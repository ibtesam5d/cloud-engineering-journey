ip addr show #to check machines IP address
hostname -I #to check machines IP address

ping google.com -c4 #ping command to ping the domain and -c flag with number means send that number of packets
ping 8.8.8.8 -c4 #with IP address

nslookup #for DNS lookup - nslookup google.com
dig #also used for DNS lookup but with different formating than nslookup
resolvectl status #to see upstream DNS server

ss -tuln #to check what ports are open and listening
netstat -tuln #older alternative to check open ports

traceroute google.com #to trace the packets hoping from server to server to reach destination

nc -zv google.com 443
nc -zv google.com 22 #to check if a certain port is open on a domain
