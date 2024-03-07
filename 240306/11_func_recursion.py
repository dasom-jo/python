#재귀함수:자기 스스로를 호출하는 함수

def recursion_sum(num):
    if num == 1:
        return 1 
    result = recursion_sum(num-1) #recursion_sum(5) 4번째자리요소
    return num + result 

print(recursion_sum(5))
#[1,2,3,4,5]

#recursion_sum(5)= num(5) + sum(4+3+2+1) = 15
#recursion_sum(4)= num(4) + sum(3+2+1) = 10
#recursion_sum(3)= num(3) + sum(2+1) = 6
#recursion_sum(2)= num(2) + sum(1) = 3
#recursion_sum(1)= 1 
