num_list = [ int(input()) for _ in range (9)]
#max를사용하여
n_max = max(num_list)
print(n_max)
print(num_list.index(n_max) + 1)

#list를 이용하여
#앞에 숫자와 뒤엣값을 반복
n_max = num_list[0]
for num in num_list:
    if num > n_max:
        n_max = num
print(n_max)        
        
