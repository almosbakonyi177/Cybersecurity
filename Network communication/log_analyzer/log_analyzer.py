from pathlib import Path
import re

script_dir=Path(__file__).resolve().parent
file_path=script_dir / "authentication_log.txt"

file=open(file_path, "r")
failed_data=[]
failed_IPs={}

for line in file:
    parts=line.strip().split(" ")
    x = re.search('Failed password', line)

    if x:
        failed_data.append(parts)
        failed_IP=parts[10]

        # Track the failed login attempts for IP addresses
        failed_IPs[failed_IP]=failed_IPs.get(failed_IP,0)+1

for ip, number in failed_IPs.items():
    if(number>4):
        print(ip," ",number)