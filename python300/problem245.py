import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
# %Y: 앞의 빈자리를 0으로 채우는 4자리 연도 숫자
# %m:앞의 빈자리를 0으로 채우는 2자리 월 숫자
# %d: 앞의 빈자리를 0으로 채우는 2자리 일 숫자