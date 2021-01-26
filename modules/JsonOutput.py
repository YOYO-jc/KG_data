import json

from modules.FileDict import update


def jsonOutputFormat(data):
    data = json.loads(data)
    # ensure_ascii 中文转码
    data = json.dumps(data, indent=4, ensure_ascii=False)
    return data


def saveAsFile(data, filename):
    data = jsonOutputFormat(data)
         
    with open("./data/%s" %filename, "w", encoding="utf-8") as f:
        f.write(data)
    
    update(filename)
