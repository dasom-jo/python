#여러 매개변수
def hello_names(count = 1, *names):
    for name in names:
        print('hello' * count, name)

        
#hello_names('손흥민','이강인','황희찬',2) 
#can't multiply sequence by non-int of type 'str'
#손흥민은 카운터가 될수없은 str

#hello_names(2,'손흥민','이강인','황희찬') 
# 실행

#hello_names(count=2'손흥민','이강인','황희찬') 
#문법 오류 문법상키워드는  무조건뒤에있어야한다

#hello_names('손흥민','이강인','황희찬',count = 2) 
#hello_names() got multiple values for argument 'count'
#매개변수 입력순서 오류 

#hello_names('손흥민','이강인','황희찬')
#카운터에 손흥민 들어가서 에러 