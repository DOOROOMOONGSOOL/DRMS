import front
import search
from operator import itemgetter
import copy
import levenshtein
import nGram
#import Euclidean


def preprocess(text):
    return ''.join(filter(str.isalnum, text))


title_list = []

f = open("data.txt", 'rt', encoding='UTF8')

while True:
    title = f.readline().rstrip()
    content = f.readline().rstrip()
    #content = "논문내용"
    processed = preprocess(title)

    if not title:
        break
    title_list.append({'title': title, 'content': content,
                      'processed': processed, 'similarity': 0})

f.close()

front.start()

while True:
    print("■ 검색할 키워드를 입력하세요 : ", end="")
    keyword = input()
    titles = search.search(title_list, keyword)

    print("\n")
    print('\033[94m' +
          "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■" + '\033[0m', end="\n\n\n")
    print("----- 검색 결과 -----")
    front.searchedTitle(titles)
    print("\n")
    print('\033[94m' +
          "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■" + '\033[0m')

    print("\n■ 읽을 논문의 번호를 입력하세요 : ", end="")
    title_num = int(input())
    while(True):
        front.searchedPaper(titles, title_num)

        titles = levenshtein.levenshtein(titles, title_num)
        #titles = nGram.nGram(titles, title_num)
        #titles = Euclidean.euclidean(titles, title_num)

        c_titles = copy.deepcopy(titles)

        titles.sort(key=lambda x: x["similarity"], reverse=True)
        for i in range(len(titles)):
            if c_titles[title_num-1]["title"] == titles[i]["title"]:
                title_index = i
                break

        front.paperRelation(titles, title_index)

        print("\n■ 다음에 읽을 논문의 번호를 입력하세요(키워드 검색으로 돌아가기는 0, 종료는 q를 입력하세요) : ", end="")
        select = input()
        if select == 'q' or select == "Q":
            print("\nDRMS 서비스를 이용해주셔서 감사합니다 =)\n")
            exit()
        elif select == '0':
            print("\n")
            break
        elif 0 < int(select) < len(titles):
            select = int(select)
            if(select < title_index):
                title_num = select
            else:
                title_num = select + 1
        else:
            print("잘못된 input입니다.")
            exit()
