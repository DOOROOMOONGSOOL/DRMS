def ComputeSp(pattern):
    sp = [-1 for _ in range(len(pattern))]
    k = -1
    for i in range(1, len(pattern) - 1):
        while k >= 0 and not pattern[k + 1] == pattern[i]: k = sp[k]
        if pattern[k + 1] == pattern[i]: k += 1
        sp[i] = k
        return sp


def preprocess(text):
    return ''.join(filter(str.isalnum, text))


def kmp(text, pattern):
    sp = ComputeSp(pattern)
    j = -1
    for i in range(len(text)):
        while j >= 0 and not pattern[j + 1] == text[i]: j = sp[j]
        if pattern[j + 1] == text[i]: j += 1
        if j == len(pattern) - 1:
            return True


def run():
    f = open("test.txt", "r")
    textList = f.readlines()
    textList = list(map(lambda x: x[:-1], textList))
    f.close()
    texts = []
    textSimilarity = []
    pattern = "코로나"
    for idx, text in enumerate(textList):
        print(text)
        tmp = preprocess(text)
        if kmp(tmp, pattern): texts.append(text)

    print("!!")
    for t in texts:
        print(t)


# run()
