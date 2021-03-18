import shutil
import os
import time

def listFiles (path):
    filesList = list()
    listData = os.listdir(path)
    for data in listData:
        if os.path.isfile(os.path.join(path, data)):
            filesList.append(data)
    return filesList

text = open('paths.txt', 'r') #We'll only read the paths to copy and paste
paths = text.read().split('|')

pathToCopy = paths[0].strip()
pathToPaste = paths[1].strip()

filesList = listFiles(pathToCopy)

for data in filesList:
    shutil.copy2(os.path.join(pathToCopy, data), pathToPaste)

text.close()

print('Data Copied Succesfully. Closing executable...')

time.sleep(5)

os.system('exit')

