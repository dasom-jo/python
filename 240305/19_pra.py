#동명이인 :공백을 기준으로 여러명의 이름을 입력받은뒤,
#동명이인을 찾아 집합으로 반환하는 프로그램을 만들어보세요


user_name = input().split()
same_list = []

#1번방법 : 모든것을 다 비교하는방법
for i in range(len(user_name)):
    for j in range(i+1, len(user_name)):
        if user_name[i] == user_name[j]:
            same_list.append(user_name[i])
# 동명이인이 여러명이면 에러날 확률 나옴
print(same_list)

# #1-1번방법
same_list = [user_name[i] for i in range(len(user_name)) 
                for j in range(i+1, len(user_name)) 
                    if user_name[i] == user_name[j]]

print(same_list)

#2번방법
same_name = set()
for name in user_name:
    if user_name.count(name) > 1:
        same_name.add(name)
print(same_name)

# #2-1번
same_name = [name for name in user_name if user_name.count(name) > 1 ]
print(same_name)
result =set(same_name)
print(result)

#
names_dict = {} #{t:2 m:2 j:1} 
result = set()

for i in names : 
    if i in names_dict:
        result.add(i)
    else
        names_dixt(i) = 1

print(result)

#
names = input()
n_dict={}
people = set()

for b in names:
    if n in n_dict:
        n_dict[n] += 1 #딕셔너리에 이미있을때
        people,.add(n)
    else:
        n_dict[n] = 1 # 딕셔넝리에 하나도 없을뗴

# for k.v in n_dict.items():
#     if v >=2:
#     print(k,v)
    #m : 2 j : 1 t : 2
    