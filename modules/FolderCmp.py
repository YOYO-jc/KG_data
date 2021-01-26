import os
import filecmp


def fileListCmp(pathA, pathB):
    a = os.listdir(pathA)
    b = os.listdir(pathB)

    A = {}
    for i in a:
        A[i] = 1
    B = {}
    for i in b:
        B[i] = 1
 
    for i in a:
        if i not in B:
            print(i, "in %s not in %s" %(pathA, pathB))
    for i in b:
        if i not in A:
            print(i, "in %s not in %s" %(pathB, pathA))
    """
    for i in b:
        if "副本" in i:
            print(i)
            os.remove("./data - 副本/%s" %i)
    """
    print("fileListCmp finished.")


def fileContentCmp(pathA, pathB):
    a = os.listdir(pathA)

    for i in a:
        if not filecmp.cmp("%s/%s" %(pathA, i), "%s/%s" %(pathB, i)):
            print(i)

    print("fileContentCmp finished.")


if __name__ == "__main__":
    fileListCmp("./data", "./data - 副本")

    fileContentCmp("./data", "./data - 副本")

