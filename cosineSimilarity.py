import re
import math

cosineSimilarity_Cnt = 0

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text
    

def cosineSimilarity(textList, patternIdx):
    
    global cosineSimilarity_Cnt
    
    for i in range(len(textList)):
        textList[i]["processed"] = cleanText(textList[i]["title"])
    #print(textList)

    splitBlank = []
    for i in range(len(textList)):
        splitBlank.append(textList[i]["processed"].split())
    
    patternDic = {}
    for i in splitBlank[patternIdx-1]:
        if i not in patternDic:
            patternDic[i] = 1
        else:
            patternDic[i] += 1

    textDic = []
    for i in splitBlank:
        tmp = {}
        for w in i:
            cosineSimilarity_Cnt += 1
            if w not in tmp:
                tmp[w] = 1
            else:
                tmp[w] += 1
        textDic.append(tmp)

    numeratorList = []
    denominatorList = []

    for i in textDic:
        tmp = 0
        for key, value in patternDic.items():
            cosineSimilarity_Cnt += 1
            if key in i:
                tmp += (value * i[key])
        numeratorList.append(tmp)
    #print(numeratorList)

    patternPower = 0
    for i in patternDic.values():
        patternPower += i**2

    textPower = []
    for i in textDic:
        tmp = 0
        for n in i.values():
            tmp += n**2
        textPower.append(tmp)

    for i in textPower:
        denominatorList.append(math.sqrt(i) * math.sqrt(patternPower))

    for i in range(len(textList)):
        textList[i]["similarity"] =  numeratorList[i] / denominatorList[i]

    print("Cosine Similarity Algorithm")
    return textList

def printCosineCnt(textList, patternIdx):
    simility = cosineSimilarity(textList, patternIdx)
    print("Compare Count : ", end="")
    print(cosineSimilarity_Cnt)
    return simility
    