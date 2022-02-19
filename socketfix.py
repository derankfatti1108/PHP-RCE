import os
import sys
#this was simple to patch fucking socket methods have fun
os.system("netstat -n -p | grep SYN_REC | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq >> black.txt")
ips = open("black.txt", "r").readlines()
for ip in ips:
	os.system(f"iptables -I INPUT -s {ip} -j DROP")
