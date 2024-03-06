def say_hi():
    nation = input('국적입력바람-> ')
    if nation.lower() == "korea" or nation == '한국':
        return hi_korean()
    else:
        return hi_english()
def hi_korean():
    print('안녕')
    
def hi_english():
    print("hi")
    
say_hi()