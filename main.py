import front
import search

title_list=[]

f = open("data.txt", 'rt', encoding='UTF8')

while True:
    line1 = f.readline().rstrip()
    #line2 = f.readline().rstrip()
    line2 = "논문내용"
    if not line1:
        break
    title_list.append([line1, line2])

front.start()

print("■ 검색할 키워드를 입력하세요 : ", end = "")
keyword = input()
titles = search.search(title_list, keyword)

print("\n----- 키워드가 포함된 논문 목록 -----")
front.search1(titles)

print("\n■ 읽을 논문의 번호를 입력하세요 : ", end = "")
title_num = input()
front.search2(titles, title_num)


f.close()