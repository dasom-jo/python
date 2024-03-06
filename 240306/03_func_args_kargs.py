# def hellos(*names): #튜플
#     print(type(names))
#     for n in names: 
#         print(f'{n}님 안녕')
        
# hellos('조다솜','이대희')

def hello_players(**players):
    print(players)
    
hello_players(손흥민 = 'fw', 이강인 = 'mf', 황희찬 = 'mf')
#딕셔너리로 정의되어 나타남

def hello_players(**players):
    for k,v in players.items():
        print(f'hi,m {v}-{k}')
    
hello_players(손흥민 = 'fw', 이강인 = 'mf', 황희찬 = 'mf')

