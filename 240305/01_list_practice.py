pra_list = [1,2,3,'파이','apple',['가', '나','다','라']]

print(len(pra_list)) #6게

#파이를 3.14로 바꾸기
pi_index=pra_list.index('파이')
pra_list[pi_index] = 3.14

print(pra_list) #[1, 2, 3, 3.14, 'apple', ['가', '나', '다', '라']]

#3을 4,8로 수정
pra_list[2] = [4,8]
print(pra_list) #[1, 2, [4, 8], 3.14, 'apple', ['가', '나', '다', '라']]
#원하는바가 아님 3의자리에 [4,8]이라는 요소가 들어온다 
pra_list[2:3] = [4,8] #슬라이싱을 이용 3의자리에 4,8이 들어오고 리스트의길이는 7
print(pra_list) #[1, 2, 4, 8, 3.14, 'apple', ['가', '나', '다', '라']]
print(len(pra_list)) #7


#"apple" 삭제하기
apl_index = pra_list.index('apple')
pra_list[apl_index:apl_index+1]=[] # apple자리에 []요소가 들어옴,ㄱ뒤에건 포함되지않으므로
print(pra_list) #[1, 2, 4, 8, 3.14, ['가', '나', '다', '라']]

#라 를 삭제하기
#del pra_list[-1]
#print(pra_list)#[1, 2, 4, 8, 3.14]
del pra_list[-1][-1]
print(pra_list)#[1, 2, 4, 8, 3.14, ['가', '나', '다']]

#나,다 삭제하기
del pra_list[-1][1:]
print(pra_list) #[1, 2, 4, 8, 3.14, ['가']]

#인덱싱은 요소 자체를 반환하지만, ㅅ,ㄹ라이싱은 요소를 리스트로 묶어서 반환한다

