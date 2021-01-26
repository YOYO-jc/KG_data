from modules import knowledgeRequest, jsonOutputFormat


if __name__ == "__main__":
    data = knowledgeRequest("胸痛", "症状")
    data = jsonOutputFormat(data)

    with open("./sample/胸痛.txt", "w", encoding="utf-8") as f:
        f.write(data)
    
