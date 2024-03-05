h_info = ['홍길동',10]
name,age = h_info
print(name,age)

eight_divior = [1,2,4,8]
odd, *even = eight_divior
print(odd, even)

yoo_info = ['유재석','tmi1',30,'tmi2','서울']
name, _, age,_, address = yoo_info
print(name, age, address)

p_info = ['박서준','잘생김','키큼','트렌디','이태원']
name,*_,work = p_info
print(name,work)