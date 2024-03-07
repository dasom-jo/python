#리스트가 정렬이되야한다 중복이나 아무순서로 되있으면 오류가 생김 

def num (list, value):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end)//2
        print(mid)
        if value == list[mid]:
            return mid
        elif value > list[mid]:
            start = mid + 1
        else: end = mid - 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9,]
my_value = 6
print(num(my_list, my_value))



