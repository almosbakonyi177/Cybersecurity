from pathlib import Path
import re

# Finds the last try's time stamp before an upper bound time stamp for an ip
def findLastTryTime(timeList, upperTimeStamp)->int:
    timeList=reversed(timeList)

    for timeStamp in timeList:
        if timeStamp<upperTimeStamp:
            return timeStamp
    return None


def patternAnalyze(timeList)->int:
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
counter=0

for line in file:
    parts=line.strip().split(" ")
    timeStampParts=parts[2].strip().split(":")
    timeStamp=int(timeStampParts[0])*3600+int(timeStampParts[1])*60+int(timeStampParts[2])

    parts[2]=timeStamp

    x = re.search('Failed password', line)

    if x:
        failed_IP=parts[10]
        
        # Track the failed login attempts for IP addresses
        failed_IPs[failed_IP]=failed_IPs.get(failed_IP,[])
        failed_IPs[failed_IP].append(parts[2])

analyzedIPs=[]
suspicious=[]

for candidate, timeStamps in failed_IPs.items():
    if candidate not in analyzedIPs:
        analyzedIPs.append(candidate)

        if patternAnalyze(timeStamps):
            suspicious.append(candidate)


print("Suspicious login attempts:")
for ip in suspicious:
    print(ip)

file.close()