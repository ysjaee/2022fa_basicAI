class Stock:
    def __init__(self,종목명,종목코드):
        self.종목명 = 종목명
        self.종목코드 = 종목코드
삼성 = Stock("삼성전자","005930")
print(삼성.종목명)
print(삼성.종목코드)
