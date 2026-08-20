import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import numpy


def importFile():
    path=filedialog.askopenfilename(title='Select the file', filetypes=[('txt files', '*.txt')])
    if path:
        readFile(path)

def readFile(path):
    global file
    try:
        file=open(path, "r")
        filePathLabel.config(text=path)
        mainTask()

    except Exception as e:
        filePathLabel.config(text=f'Error: {e}')

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
    global outputText

    # First read in the file
    for line in file:
        parts=line.strip().split()
        timeStampParts=parts[2].strip().split(":")
        timeStamp=int(timeStampParts[0])*3600+int(timeStampParts[1])*60+int(timeStampParts[2])

        x = re.search('Failed password', line)

        if x:
            failed_IP=re.search(r'from (\d+\.\d+\.\d+\.\d+)', line).group(1)
            day=parts[1]

            # Track the failed login attempts for IP addresses
            failed_IPs[day]=failed_IPs.get(day, {})
            failed_IPs[day][failed_IP]=failed_IPs[day].get(failed_IP,[])
            failed_IPs[day][failed_IP].append(timeStamp)


    suspicious=set()

    for day, IP_data in failed_IPs.items():
        for candidate, timeStamps in IP_data.items():
        
            if patternAnalyze(timeStamps):
                # If there was too many tries in too short time it is suspicious
                suspicious.add(day+" "+candidate)

        percentile=numpy.percentile(list(len(attempts) for attempts in IP_data.values()), 95)
        for candidate, attempts in IP_data.items():
            if len(attempts)>percentile:
                suspicious.add(day+" "+candidate)

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