def hello(name = '', count = 1):
    if name != '':
        name+= "님 "
    for _ in range(count):
        print( f'{name}안녕')
        
hello()
hello('조다솜')
hello('홍길동',3)