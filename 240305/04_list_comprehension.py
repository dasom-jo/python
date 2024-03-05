num_list = [1,2,3,4]
#even_list = []

#리스트 = [변수를 활용한식 for 변수명 in 반복객체]
for e in num_list:
    #print(e)
    #print(e*2)
    #even_list.append(e*2)
    #print(even_list)
    even_list = [e*2 for e in num_list]
    print(even_list)