def getRequestName(name):
    name = name.replace("﻿", "")
    name = name.replace("+", "＋")
    return name


def getSaveName(name):
    name = getRequestName(name)
    name = name.replace("\n", "")
    name = name.replace("/", "&")  
    return "%s.txt" %name