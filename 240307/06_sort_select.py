#선택정렬
def selction_sorted(list) :
    length = len(list)
    for x in range(length - 1):
        #마지막 요소는 이미 이전 단계에서 최소값으로 선택되었기 때문에 
        #추가적인 비교 없이 외부 루프가 종료될 수 있습니다.
        min = x #선택된위치가 최초 최소값 지정 0번째자리
        for y in range(x + 1,length):
            if list[min] > list[y]:
                min = y # 최솟값이라고 생각햇는 다른 최소값이 나타나가지고 자리뺏김
                print(f'이제 최소값은 {list[y]}이다')
            list[x],list[min] = list[min],list[x]#보이는 자리도 바꾸자 
        return list
    
print(selction_sorted([5,4,3,2,6,3,1]))

