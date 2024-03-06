'''함수정의
def 함수이름(매개변수 1,2)
    #코드블록
    return 결과값
    
    함수 호출
    함수이름(매개변수1,2)'''
    
#함수의정의
def hello1():
    print('안녕')
    
def hello2(name):
    print(f'{name}님 안녕')
    
def hello3(name,count):
    for _ in range(count):
        print(f'{name}님 안녕')
        
hello1()
hello2('조다솜')
hello3('홍길동',3)