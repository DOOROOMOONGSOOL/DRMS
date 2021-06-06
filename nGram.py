# input string 공백 및 특수기호 제거 x

def splitString(str, idx):
    strList = []

    for i in range(len(str)-idx+1):
        strList.append(str[i:i+idx])
    
    return strList

def nGram(pattern, text, idx):

    patternList = splitString(pattern, idx)
    textList = splitString(text, idx)

    unionList = patternList.copy()
    intersectionList = []

    for w in textList:
        if w in unionList:
            intersectionList.append(w)
            continue
    
    return len(intersectionList) / len(unionList)


print(nGram("나는멍청이이다", "나는뭉청이이다",2))


