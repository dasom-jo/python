
def find_num(list, value):
    """
        (선형탐색 혹은 순차 탐색)
        list 내에서 value값에 해당하는 위치를 반환
        없으면 -1반환
    """
    #리스트의 길이
    l = len(list)
    
    #리스트의 모든 원소와 일일이 대조
    for i in range(l):
        if value == list[i]:
            #일치하는 index응 발견하면 즉시 return
            return i
        return -1
    
my_arr = [1,54,3,4,1,63,4,34]
print(find_num(my_arr, 63))