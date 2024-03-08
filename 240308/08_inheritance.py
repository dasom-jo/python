#oop: object oriented progranmming(객체지향프로그래밍)

#전자제품(ElecProduct)  클래스
#   [price:가격, product_name: 상품명]
#   [info()가격과 상품명을 출력하는 메서드 ]

#휴대폰(SmartPhone)클래스 - 전자체품 클래스 상속
#[phone_name:,volumn:용량]
#[call():여보세요 출력 메서드]
#[info(): 가격과 상품명 폰이름,용량까지 출력하는 메서드] 오버라이딩


class ElecProduct:
    def __init__(self, price = '-$', product_name = '-plus',volumn = "-GB"):
        self.price = price
        self.product_name = product_name
        self.volumn = volumn
    
    def info(self):
        print(f'price :{self.price}, product_name :{ self.product_name},volumn : {self.volumn}')
        


class SmartPhone:
    def __init__(self):
        super().__init__()
        self.price = '400$'
        self.product_name = 'ipone13_plus'
        self.date = '2023-01-01'
        self.volumn = "64GB"
        
    def call(self):
        print("여보세요?")
        
    def info(self):
        print(f'price :{self.price}, product_name :{self.product_name},volumn: {self.volumn}, date :{self.date}')
        

ep = ElecProduct()
ep.info()

ipone = SmartPhone()
ipone.call()
ipone.info()

print(isinstance(ep,ElecProduct))
print(isinstance(ipone,ElecProduct))
print(isinstance(ipone,SmartPhone))