N=input("숫자를 하나 입력해주세요").split()

A = [int(i) for i in input(f'({N}개의 숫자를 입력해주세요)').split()]

M = input("숫자를 하나 입력해주세요").split()

M1=[int(i) for i in input(f'({M}개의 숫자를 입력해주세요)').split()]

#print(M1)

#B의 크기 * A의 배열크기 O(n**2)

for i in M1: #for  O(n)
    if i in A: #in의 복잡도 : O(n)
        print(1)
    else:
        print(0) 
        #M1입장출력
        

#함수로 바꾸기

