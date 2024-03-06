#재귀함수:자기 스스로를 호출하는 함수

def recursion_multiply(num):
    if num == 1:
        return 1 
    result= recursion_multiply(num - 1)
    return num * result

print(recursion_multiply)


