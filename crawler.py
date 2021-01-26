import os
import json

from modules import *


# 疾病类 分为 常见病、科室、ICD10
# 请求“疾病”list == “常见病”list
def get_list():
    types = ["疾病", "药物", "症状", "诊疗", "常见病", "科室", "ICD10"]
    for i in types:
        data = listRequest(i)    
        data = jsonOutputFormat(data)

        with open("./list/%s.txt" %i, "w", encoding="utf-8") as f:
            f.write(data)


# list文件里只有nodes
# 目标为datarange.png
def get_data():
    filelist = os.listdir("./list")
    for filename in filelist:
        # filename = os.path.splitext(filename)[0]
        with open("./list/%s" %filename, "r", encoding="utf-8") as f:
            data = json.loads(f.read())

        for node in data["nodes"]:
            if "name" not in node:
                continue
            if node["name"] == "":
                continue      
            if not node["icon"].endswith("datarange.png"):
                continue
            
            if not isExist(getSaveName(node["name"])):
                res = None
                while res is None:
                    # print(filename)
                    res = knowledgeRequest(getRequestName(node["name"]))
                saveAsFile(res, getSaveName(node["name"]))


if __name__ == "__main__":
    get_list()
    get_data()
