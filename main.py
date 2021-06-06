import front
import search
import levenshtein
import nGram
import Euclidean

def preprocess(text):
    return ''.join(filter(str.isalnum, text))

title_list=[]

f = open("data.txt", 'rt', encoding='UTF8')

while True:
    title = f.readline().rstrip()
    #content = f.readline().rstrip()
    content = "논문내용"
    processed = preprocess(title)
    
    if not title:
        break
    title_list.append({'title' : title, 'content' : content, 'processed' : processed, 'similarity' : 0})

f.close()    

front.start()

while True:
    print("■ 검색할 키워드를 입력하세요 : ", end = "")
    keyword = input()
    titles = search.search(title_list, keyword)

    print("\n----- 키워드가 포함된 논문 목록 -----")
    front.searchedTitle(titles)

    
    print("\n■ 읽을 논문의 번호를 입력하세요 : ", end = "")
    title_num = int(input())
    while(True):
        front.searchedPaper(titles, title_num)

        #titles = levenshtein.levenshteion(titles, title_num)
        #titles = nGram.nGram(titles, title_num)
        #titles = Euclidean.euclidean(titles, title_num)
        
        front.paperRelation(titles, title_num)

        print("\n■ 다음에 읽을 논문의 번호를 입력하세요(키워드 검색으로 돌아가기는 0, 종료는 q를 입력하세요) : ", end = "")
        select = input()
        if select == 'q' or select == "Q":
            exit()
        elif select == '0':
            break
        else:
            select = int(select)
            if(select < title_num):
                title_num = select
            else:
                title_num = select + 1

