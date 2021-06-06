import copy

def search(title_list, keyword):
    titles=[]
    for i in title_list:
        kor = copy.deepcopy(i[0])
        #kor = translate.translate(kor)
        
        if keyword in kor:
            titles.append([i[0], kor, i[1]])
    
    return titles
