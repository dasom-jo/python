empty_dict1={}
empty_dict2=dict()

son_dict = {
    'name' : '손흥민',
    'age' : 29,
    'address' : ['한국','영국','독일']
}

print(son_dict)

#키를 통한 값 조회
print(son_dict['name'])

#딕셔너리에 데이터 추가
son_dicrt['job'] = '축구선수'

#딕셔너리 내 값 수정
son_dict['name'] = 'son'

#딕셔너리내 데이터 삭제
del son_dict['address'] 