import sys
new_input = sys.stdin.readline

data = new_input().strip() #엔터치면 줄바꿈 ㅎ나번 더 늘어나서 
print(data)

def sayhi():
    print('안녕')
sh = sayhi
sh()

def plus(a,b):
    return a + b

def minus(a,b):
    return a -b

# calc_list = [plus, minus]
# print(calc_list[0](10,20))
# print(calc_list[0](10,20))

calc_list = {'합' : plus,"차" : minus}
print(calc_list['합'](10,20))
print(calc_list["차"](10,20))

