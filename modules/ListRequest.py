import requests


#tree_type 例：药物 症状 诊疗
def listRequest(tree_type):
    url = "https://zstp.pcl.ac.cn:8002/load_tree/" + tree_type
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
        res = requests.get(url, headers=header, timeout=5)
        res.encoding = "utf-8"
        return res.text
        
    except Exception as e:
        print(e)
        exit()


if __name__ == "__main__":
    res = listRequest("症状")
    # print(res)