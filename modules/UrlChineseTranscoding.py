from urllib.parse import quote, unquote


def urlChineseTranscoding(s):
    return unquote(s, encoding="utf-8")


if __name__ == "__main__":
    s = "%E7%A7%91%E5%AE%A4"

    s = urlChineseTranscoding(s)
    print(s)
