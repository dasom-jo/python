#리스트 = [변수를 활용한식 for 변수명 in 반복객체]

name_list = [ '손흥민', '조규성', '김민재', '이강인', '이승우', '황희찬' ]

lee_list= [name for name in name_list if name[0] == '이']
son_list= [name for name in name_list if name[0] == '이' or name[0] == '손' ]
print(lee_list)
print(son_list)