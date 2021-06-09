# input string 공백 및 특수기호 제거 x

idx = 2
nGram_Cnt = 0

def splitString(str):
    strList = []

    for i in range(len(str)-idx+1):
        strList.append(str[i:i+idx])
    
    return strList


def nGram(textList, patternIdx):

    global nGram_Cnt

    patternIdx = patternIdx - 1
    pattern = splitString(textList[patternIdx]["processed"])

    splitTextList = []
    for i in textList:
        splitTextList.append(splitString(i["processed"]))

    # unionList = pattern.copy()
    unionList = []
    intersectionList = []

    for w in splitTextList:
        tmp = []
        unionTmp = pattern.copy()
        nGram_Cnt += len(unionTmp)
        for p in w:
            nGram_Cnt += 1
            if p in pattern:
                tmp.append(p)
            else:
                unionTmp.append(p)

        unionList.append(unionTmp)
        intersectionList.append(tmp)
        unionTmp = []
    
    for i in range(len(textList)):
        textList[i]["similarity"] = len(intersectionList[i]) / len(unionList[i])
    
    print("nGram Algorithm")
    return textList

def printNgramCnt(textList, patternIdx):
    simility = nGram(textList, patternIdx)
    print("Compare Count : ", end = "")
    print(nGram_Cnt)
    return simility

