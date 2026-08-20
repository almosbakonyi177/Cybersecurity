from pathlib import Path
import re

# Finds the last try's time stamp before an upper bound time stamp for an ip
def findLastTryTime(timeList, upperTimeStamp)->int:
    timeList=reversed(timeList)

    for timeStamp in timeList:
        if timeStamp<upperTimeStamp:
            return timeStamp
    return None

# Looks for brute force login tries in a timestamps list using sliding window
def checkBruteForce(timeList)->bool:
    timeList=sorted(timeList)
    windowSize=3600
    threshold=5
    left=0

    for right in range(len(timeList)):
        while timeList[right]-timeList[left]>windowSize:
            left+=1
        counter=right-left+1
        if counter>=threshold:
            return True

    return False


script_dir=Path(__file__).resolve().parent
file_path=script_dir / "authentication_log.txt"

file=open(file_path, "r")
failed_IPs={}

# First read in the file
for line in file:
    parts=line.strip().split(" ")

    if len(parts)<3:
        continue

    timeStampParts=parts[2].strip().split(":")
    timeStamp=int(timeStampParts[0])*3600+int(timeStampParts[1])*60+int(timeStampParts[2])

    x = re.search('Failed password', line)

    if x:
        failed_IP=re.search(r'from (\d+\.\d+\.\d+\.\d+)', line).group(1)

        # Track the failed login attempts for IP addresses
        failed_IPs[failed_IP]=failed_IPs.get(failed_IP,[])
        failed_IPs[failed_IP].append(timeStamp)


suspicious=[]

for candidate, timeStamps in failed_IPs.items():

    if checkBruteForce(timeStamps):
        # If there was too many tries in 1 hour it is suspicious
        suspicious.append(candidate)


print("Suspicious login attempts from these IPs:")
for ip in suspicious:
    print(ip)

file.close()