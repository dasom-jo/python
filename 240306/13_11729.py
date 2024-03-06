N = int(input())

def hanoi(n):
    if n == 1:
        return 1
    first = hanoi(n-1)
    second = 1
    third = hanoi(n-1)
    return = first + second + third
    #return 1 + 2 * hanoi(n-1)

count = hanoi(N)

# def hanoi_detail(n, 시작, 중간, 목표):
#     if n == 1:
#         return 1
#     first = hanoi(n-1, 시작, 목표, 중간)
#     second = 1
#     third = hanoi(n-1, 중간, 시작, 목표)
#     return = first + second + third
#     #return 1 + 2 * hanoi(n-1)

# count = hanoi_detail(N)

def hanoi_detail(n, start, mid, goal)
    if n == 1:
        print(start,goal)
        return
    hanoi_detail(n-1,start,goal,mid)
    
