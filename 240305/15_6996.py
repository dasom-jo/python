CASE_NUM = int(input())


for i in range(CASE_NUM):
    word_a, word_b = input().split()
    d_word_a = {}
    for u in word_a:
        if i in d_word_a:
            d_word_a[i] +=1
    else:
        d_word_a[i] = 1
    
    d_word_b = {}
    #word_b를 이용한 딕셔너리 생성
    for i in range(CASE_NUM):
        word_a,word_b = input().split()
        d_word_b = {}
        for i in word_b:
            if i in d_word_b:
                d_word_a[i] +=1
            else:
                d_word_b[i] = 1
            
        d_word_b = {}

        
    
    #딕셔너리 두개비교