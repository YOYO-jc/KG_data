import os
import json


def checkData():
    filelist = os.listdir("./data")
    res = []

    for filename in filelist:
        with open("./data/%s" %filename, "r", encoding="utf-8") as f:
            #print(filename)
            data = json.loads(f.read())
            if len(data["categories"]) <= 2:
                print(filename)

                res.append(filename)
    return res


def removeWrongData(res):
    print("remove......")

    for filename in res:
    #    print(filename)
        os.remove("./data/%s" %filename)


if __name__ == "__main__":
    res = checkData()

    removeWrongData(res)
