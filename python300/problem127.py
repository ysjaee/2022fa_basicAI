주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
elif 주민번호[0] == "2" or 주민번호[0] == "4":
    print("여자")
else:
    print("1~4사이만 가능")