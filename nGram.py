# input string 공백 및 특수기호 제거 x

idx = 2

def splitString(str):
    strList = []

    for i in range(len(str)-idx+1):
        strList.append(str[i:i+idx])
    
    return strList


def nGram(textList, patternIdx):

    patternIdx = patternIdx - 1
    pattern = splitString(textList[patternIdx][processed])

    splitTextList = []
    for i in textList:
        splitTextList.append(splitString(i[processed]))

    unionList = pattern.copy()
    intersectionList = []

    for w in splitTextList:
        for p in w:
            tmp = []
            if p in pattern:
                tmp.append(p)
        intersectionList.append(tmp)
    
    for i in range(len(textList)):
        textList[i][similarity] = len(intersectionList[i]) / len(unionList[0])
        
    return textList


