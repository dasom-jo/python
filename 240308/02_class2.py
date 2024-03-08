#oop: object oriented progranmming(객체지향프로그래밍)

class Animal:
    #클래스변수
    age = 1
    #클래스함수
    def set_name(self, data):
        self.name = data
    #생성자
    #인스턴스함수
    pass

pig = Animal()
pig.set_name('꿀꿀이')

panda = Animal()
Animal.set_name(panda, '푸바오')

pig.age=5
panda.age=10

print(f'{pig.name}는{pig.age}살입니다')

print(f'{panda.name}는{panda.age}살입니다')

#1살 나와ㅇ 하는디?????
