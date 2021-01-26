import requests


#name tree_type 例：抑郁症 疾病
def knowledgeRequest(name, tree_type="疾病"):
    print("爬取中...", name)

    url = "https://zstp.pcl.ac.cn:8002/knowledge?name=" + name + "&tree_type=" + tree_type
    header = {
        "Host": "zstp.pcl.ac.cn:8002",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://zstp.pcl.ac.cn:8002/mekg?v0=%E6%99%AE%E9%80%9A%E6%84%9F%E5%86%92",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7"
    }

    try:
        res = requests.get(url, headers=header, timeout=8)
        res.encoding = "utf-8"
        return res.text

    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    res = knowledgeRequest("胸痛", "症状")
    print(res)