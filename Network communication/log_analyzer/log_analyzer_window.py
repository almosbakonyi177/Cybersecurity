from pathlib import Path
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def importFile():
    path=filedialog.askopenfilename(title='Select the file', filetypes=[('txt files', '*.txt')])
    if path:
        readFile(path)

def readFile(path):
    global file
    global variables
    try:
        file=open(path, "r")
        filePathLabel.config(text=path)
        mainTask()

    except Exception as e:
        filePathLabel.config(text=f'Error: {e}')


# Finds the last try's time stamp before an upper bound time stamp for an ip
def findLastTryTime(timeList, upperTimeStamp)->int:
    timeList=reversed(timeList)

    for timeStamp in timeList:
        if timeStamp<upperTimeStamp:
            return timeStamp
    return None

# Looks for brute force pattern in a timestamps list using sliding window
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

def mainTask():
    failed_IPs={}
    counter=0
    global outputText

    # First read in the file
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



    suspicious=[]

    for candidate, timeStamps in failed_IPs.items():

        if patternAnalyze(timeStamps):
            # If there was too many tries in too short time it is suspicious
            suspicious.append(candidate)


    print("Suspicious login attempts from these IPs:")
    for ip in suspicious:
        print(ip)

    file.close()
    outputText.config(text="\n".join(suspicious))
    return suspicious

window=tk.Tk()
window.geometry("750x750")
window.title('Mask')

baseSettingsBar=tk.Frame(window)

baseSettingsBar.pack(side='top', anchor='nw', pady=20, padx=20)

uploadButton=tk.Button(baseSettingsBar, text='Import log text File', command=importFile)
uploadButton.pack(side='left')

filePathLabel = tk.Label(baseSettingsBar, text='')
filePathLabel.pack(side='right')

outputs=tk.Frame(window)
outputs.pack(side='top', anchor='nw', pady=20, padx=20)

outputLabel=tk.Label(outputs, text='Suspicious login attempts from these IPs:')
outputLabel.pack(side='top', anchor='nw', pady=20, padx=20)

outputText=tk.Label(outputs, text='')
outputText.pack(side='top', anchor='nw', pady=20, padx=20)

window.mainloop()