def ComputeSp(pattern):
    sp = [-1 for _ in range(len(pattern))]
    k = -1
    for i in range(1, len(pattern) - 1):
        while k >= 0 and not pattern[k + 1] == pattern[i]:
            k = sp[k]
        if pattern[k + 1] == pattern[i]:
            k += 1
        sp[i] = k
    return sp


def kmp(text, pattern):
    sp = ComputeSp(pattern)
    j = -1
    for i in range(len(text)):
        while j >= 0 and not pattern[j + 1] == text[i]:
            j = sp[j]
        if pattern[j + 1] == text[i]:
            j += 1
        if j == len(pattern) - 1:
            return True


def search(textList, keyword):
    searched = []
    for text in textList:
        if kmp(text["processed"], keyword):
            searched.append(text)

    return searched
