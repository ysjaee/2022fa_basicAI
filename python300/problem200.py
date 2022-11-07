# 시가(open), 고가 (high), 저가 (low) , 종가(close)
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
result = 0
for row in ohlc[1:]:
    result += (row[3] - row[0])
print(result)