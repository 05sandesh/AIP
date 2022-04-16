import subprocess
import os, time, threading
from os import path
import psutil
import json
import time
  

def get():
    # p = psutil.Process(<ProcessID>)
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[2]
    disk1 = psutil.disk_usage('/')  
    # print(disk1)
    dictionary ={
        "CPU usage" : cpu,
        "RAM usage" : ram,
        "Disk" : disk1[3],
    }
    json_object = json.dumps(dictionary, indent = 3)

    filename = str(time.time())+'py.json'
    # if path.isfile(filename) is False:
    with open(filename, "w") as outfile:
        outfile.write(json_object)
    # else:
    #     with open(filename) as fp:
    #         listObj = json.dumps(json.loads(fp))

    #     print(listObj)
    #     listObj['Process'].append(json_object)
    #     with open(filename, 'w') as json_file:
    #         json.dump(listObj,json_file)
    


if __name__=="__main__":
    get()