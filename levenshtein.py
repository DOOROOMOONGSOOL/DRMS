# 최소편집거리를 이용한 문장 간의 유사도
def getSimilarity(text, pattern):
    med, max = editDist(text, pattern)
    return 1 - (med / max)


# 문장 전처리를 위한 함수
# 문장 내의 모든 특수문자와 공백을 제거
def preprocess(text):
    return ''.join(filter(str.isalnum, text))


def editDist(text, pattern):
    iCost, dCost = 1, 1
    dTable = [[0 for _ in range(len(text) + 1)] for _ in range(len(pattern) + 1)]

    for i in range(1, len(text) + 1):
        dTable[0][i] = dTable[0][i - 1] + iCost
    for i in range(1, len(pattern) + 1):
        dTable[i][0] = dTable[i - 1][0] + dCost

    for i in range(1, len(pattern) + 1):
        for j in range(1, len(text) + 1):
            cCost = iCost + dCost if pattern[i - 1] != text[j - 1] else 0
            dTable[i][j] = min(dTable[i - 1][j] + dCost, dTable[i][j - 1] + iCost, dTable[i - 1][j - 1] + cCost)

    # for i in range(len(dTable)):
    #     print(dTable[i])

    return dTable[len(pattern)][len(text)], dCost * len(pattern) + iCost * len(text)


def main():
    # txt에서 기사, 논문 제목을 읽어들임
    f = open("test.txt", "r")
    textList = f.readlines()
    textList = list(map(lambda x: x[:-1], textList))
    f.close()

    pattern = preprocess(textList[5])
    textSimilarity = []
    for idx, text in enumerate(textList):
        print(text)
        tmp = preprocess(text)
        textSimilarity.append([text, getSimilarity(tmp, pattern)])

    textSimilarity.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(textSimilarity)):
        print(textSimilarity[i])

# main()
