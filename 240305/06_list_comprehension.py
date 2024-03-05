#리스트 = [변수를 활용한식 for 변수명 in 반복객체]

#숫자 세개를 입력받고 평균 반환하는 프로그램 만들기
# user_input = input('공백을 기준으로 숫자 세 개를 입력하세요\n')
# print(user_input)
# print(user_input.split())
# user_input_list = user_input.split()

# num_list = []
# for i in user_input_list:
#     num_list.append(int(i))
    
# print(num_list)

# sum = 0 
# for i in num_list:
#     sum+=i
    
# avg = sum / len(num_list)
# print(avg)


num_list = [int(i) for i in input('숫자 세 개를 입력하세요').split()]
avg = sum(num_list)/ len(num_list)
print(avg)


