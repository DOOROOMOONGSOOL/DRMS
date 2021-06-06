import search

def start():
    '''
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■     ■■■■■■                                                ■ ■")
    print("■ ■     ■                                                     ■ ■")
    print("■ ■     ■                                                     ■ ■")
    print("■ ■     ■■■■■■                                                ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■    ■■■■■■■■■                                              ■ ■")
    print("■ ■        ■                                                  ■ ■")
    print("■ ■        ■                                                  ■ ■")
    print("■ ■        ■                                                  ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    '''
    print ("\n■ ■ ■ ■ ■ ■ ■ ◈  두루뭉술 논문 찾기  ◈  ■ ■ ■ ■ ■ ■ ■\n")


def search1(titles):
    for i in range(len(titles)):
        if(titles[i][0] == titles[i][1]):
            print(i + 1, end = ". ")
            print(titles[i][0])

        else:
            print(i + 1, end = ". ")
            print(titles[i][0], end = "  ( 번역 : ")
            print(titles[i][1], end = " )")

def search2(titles, title_num):
    print("")
    print("\n◈   Title   : ", end = "")
    print(titles[int(title_num)-1][0])
    print("\n◈  Abstract : ", end = "")
    print(titles[int(title_num)-1][2], end = "\n\n\n\n")

    print("\n----- 연관 논문 리스트 -----")
    index = 1
    for i in range(len(titles)):
        if(int(title_num) - 1 != i):
            print(index, end = ". (유사도 : ")
            #print(search.nGram(titles[int(title_num)-1][0], titles[i][0], 2), end = "%) ")
            print(titles[i][0])
            index += 1
            