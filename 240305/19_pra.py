#동명이인 :공백을 기준으로 여러명의 이름을 입력받은뒤,
#동명이인을 찾아 집합으로 반환하는 프로그램을 만들어보세요


user_name = input().split()
same_list = []

#1번방법
for i in range(len(user_name)):
    for j in range(i+1, len(user_name)):
        if user_name[i] == user_name[j]:
            same_list.append(user_name[i])

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

