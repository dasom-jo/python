son_dict = {
    'name' : '손흥민',
    'age' : 29,
    'address' : ['한국','영국','독일']
}
print(son_dict.keys())
print(len(son_dict.keys()))
print(son_dict.values())
print(son_dict.items()) #키와 밸류를 각각 튜플로 묶어서 반환

print(son_dict.get('name')) #= print(son_dict['name'])

#print(son_dict.get('job')) #에러남 다음거 실행못함
print(son_dict.get('job')) #none
print(son_dict.get('job','무직')) #업스면 기본값 출력

for k, v in son_dict.items():
    print(f'키 : {k},값 : {v}')
    
