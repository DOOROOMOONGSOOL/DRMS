import re
import math

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text
    

def cosineSimility(textList, patternIdx):

    for i in range(len(textList)):
        textList[i]["processed"] = cleanText(textList[i]["title"])
    print(textList)

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
            if key in i:
                tmp += (value * i[key])
        numeratorList.append(tmp)
    print(numeratorList)

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

    return textList

#diecc = [{'title': "i don't know that that.", 'content': "sdf", 'processed': "idontknowthat", 'similarity': 0},{'title': "i don't know know know that that.", 'content': "sdf", 'processed': "idontknowthat", 'similarity': 0}]
#print(cosineSimility(diecc, 1))
    