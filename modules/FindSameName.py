# 结论： 同名实体唯一，与类别无关：A，症状 == A，疾病
# 代谢性\n酸中毒、代谢性酸中毒 为特例


import os
import json


def renameBeforeRequest(name):
    name = name.replace("﻿", "")
    name = name.replace("+", "＋")
    return name

def renameBeforeSave(name):
    name = name.replace("\n", "")
    name = name.replace("/", "&")  
    return name


def checkFilelist():
    dic = {}
    a = ["常见病", "科室", "ICD10"]

    for filename in a:
        # filename = os.path.splitext(filename)[0]
        with open("./list/%s.txt" %filename, "r", encoding="utf-8") as f:
            data = f.read()
            data = json.loads(data)

            for node in data["nodes"]:
                if "name" not in node:
                    continue
                if node["name"] == "":
                    continue      
                if not node["icon"].endswith("datarange.png"):
                    continue
                
                node["name"] = renameBeforeRequest(node["name"])
                node["name"] = renameBeforeSave(node["name"])

                dic[node["name"]] = True
    

    with open("./list/症状.txt", "r", encoding="utf-8") as f:
        data = f.read()
        data = json.loads(data)

        for node in data["nodes"]:
            if "name" not in node:
                continue
            if node["name"] == "":
                continue      
            if not node["icon"].endswith("datarange.png"):
                continue

            node["name"] = renameBeforeRequest(node["name"])
            node["name"] = renameBeforeSave(node["name"])

            if node["name"] in dic:
                print(node["name"])


checkFilelist()