class Stock:
    def __init__(self,종목명,종목코드):
        self.종목명 = 종목명
        self.종목코드 = 종목코드
    def set_name(self,종목명):
        self.종목명 = 종목명

a = Stock(None,None)
print(a.종목명)
a.set_name("삼성전자")
print(a.종목명)