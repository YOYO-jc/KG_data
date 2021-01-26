import os


def initFileDict():
    filelist = os.listdir("./data")

    for filename in filelist:
        filename = filename.lower()
        fileDict[filename] = True


def isExist(filename):
    filename = filename.lower()
    if filename in fileDict:
        return True
    return False 


def update(filename):
    filename = filename.lower()
    fileDict[filename] = True


#包括后缀名 不包括路径  例：抑郁症.txt
fileDict = {}

initFileDict()