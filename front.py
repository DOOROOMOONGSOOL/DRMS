import search


def start():

    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■    ■ ■ ■       ■ ■ ■           ■      ■       ■ ■ ■ ■     ■ ■")
    print("■ ■    ■     ■     ■     ■         ■      ■       ■           ■ ■")
    print("■ ■    ■      ■    ■     ■        ■ ■    ■ ■      ■           ■ ■")
    print("■ ■    ■      ■    ■ ■ ■          ■ ■    ■ ■      ■ ■ ■ ■     ■ ■")
    print("■ ■    ■      ■    ■     ■       ■   ■  ■   ■           ■     ■ ■")
    print("■ ■    ■     ■     ■      ■     ■      ■     ■          ■     ■ ■")
    print("■ ■    ■ ■ ■       ■       ■    ■      ■     ■    ■ ■ ■ ■     ■ ■")
    print("■ ■                                                           ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")

    print("\n■ ■ ■ ■ ■ ■ ■ ◈  두루뭉술 논문 찾기  ◈  ■ ■ ■ ■ ■ ■ ■\n")
    # print('\033[93m \033[100m' + "\n■ ■ ■ ■ ■ ■ ■ ◈  두루뭉술 논문 찾기  ◈  ■ ■ ■ ■ ■ ■ ■\n")


def searchedTitle(titles):
    for i in range(len(titles)):
        print(i + 1, end=". ")
        print(titles[i]["title"])


def searchedPaper(titles, title_num):
    print("\n\n--------------------------")
    print("◈  제목  : ", end="")
    print(titles[int(title_num)-1]["title"])
    print("\n◈  초록  ")
    print(titles[int(title_num)-1]["content"], end="\n\n")


def paperRelation(titles, title_index):
    print("\n----- 연관 논문 리스트 -----")
    index = 1
    for i in range(len(titles)):
        if(int(title_index) != i):
            print(index, end=". (유사도 : ")
            print("%0.2f" % (titles[i]["similarity"] * 100), end="%) ")
            print(titles[i]["title"])
            index += 1
