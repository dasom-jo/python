my_set1 = set([1,2,3,4,5,6])
my_set2 = set([4,5,6,7,8,9])



#네트1과 세트2합침
#result = my_set1 | my_set2
#my_set1.update(my_set2) 세트1과 세트2 가 합쳐짐
result = my_set1.union(my_set2)
print(my_set1)
print(my_set2)
print(result)

#세트1에 세트2과 공통된부분으로 업데이트된다 
#my_set1.intersection_update(my_set2)
result = my_set1.intersection(my_set2)

print(my_set1)
print(my_set2)
print(result)


#세트1이 세트2와 다른 부분으로 업데이트 
my_set1.difference_update(my_set2)
print(my_set1)

#세트1과 세트2의 차집함
result = my_set1 - my_set2
print(result)

#세트1에 세트2의 대칭차를 업데이트
#my_set1.symmetric_difference_update(my_set2)

#세트1ㄱ과 세트 2의 대칭차 반환
result = my_set1^ my_set2
print(result)


#add: 요소 추가
#remove,discard :요소삭제 ,리무브는 없는 요소인경우 에러 발생
result.remove(9)
print(result)