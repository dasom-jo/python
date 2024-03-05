alphabet = ['A','B','C','D','E']

#sample = alphaber[1:5:3] #[ace]

#vow = alphabet[::4] 처음과 끝 생략가능
#vow = alphabet = [0:5:4]

vow = [alphabet[0],alphabet[4]] # 인덱스
consonant = alphabet[1:4] #슬라이싱

new_alphabet = [vow, consonant]
print(new_alphabet) #[['A', 'E'], ['B', 'C', 'D']]

#new_alphabet 에서 e를 추출하고싶다
#[['A', 'E'], ['B', 'C', 'D']] 첫번재 배열 0, 그배열안에 1번쨰
print(new_alphabet[0][1])

