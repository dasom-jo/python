#oop: object oriented progranmming(객체지향프로그래밍)

class Animal:
    #생성자
    def __init__(self, name= 'unnamed', age = '0'): #이함수바를 먼저 실행해줌 /기본값
        self.name = name
        self.age = age
    #클래스변수
    
    #클래스함수
    def info(self):
        print(f'name: {self.name},age:{self.age}')
    
    #인스턴스함수
    
class Human(Animal):
    def speak(self,data):
        print(f'{self.name} : {data}')
        
# choi = Human()
choi = Human('조다솜',4)
choi.info()
choi.speak('안녕하세요')