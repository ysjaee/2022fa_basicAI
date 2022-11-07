class Stock:
    def __init__(self,종목명,종목코드):
        self.종목명 = 종목명
        self.종목코드 = 종목코드
    def set_name(self,종목명):
        self.종목명 = 종목명
    def set_code(self,종목코드):
        self.종목코드 = 종목코드
    def get_name(self):
        return self.종목명
    def get_code(self):
        return self.종목코드
삼성 = Stock("삼성전자","005930")
print(삼성.종목명)
print(삼성.종목코드)
print(삼성.get_name())
print(삼성.get_code())