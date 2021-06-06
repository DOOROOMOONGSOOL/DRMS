# 최소편집거리를 이용한 문장 간의 유사도
def getSimilarity(text, pattern):
    med, max = editDist(text, pattern)

    return 1 - (med / max)


def editDist(text, pattern):
    iCost, dCost = 1, 1
    dTable = [[0 for _ in range(len(text) + 1)]
              for _ in range(len(pattern) + 1)]

    for i in range(1, len(text) + 1):
        dTable[0][i] = dTable[0][i - 1] + iCost
    for i in range(1, len(pattern) + 1):
        dTable[i][0] = dTable[i - 1][0] + dCost

    for i in range(1, len(pattern) + 1):
        for j in range(1, len(text) + 1):
            cCost = iCost + dCost if pattern[i - 1] != text[j - 1] else 0
            dTable[i][j] = min(dTable[i - 1][j] + dCost, dTable[i]
                               [j - 1] + iCost, dTable[i - 1][j - 1] + cCost)

    return dTable[len(pattern)][len(text)], dCost * len(pattern) + iCost * len(text)


def levenshteion(textList, idx):
    pattern = textList[idx]["title"]
    for i, text in enumerate(textList):
        textList[i]["similarity"] = getSimilarity(text, pattern)

    return textList
