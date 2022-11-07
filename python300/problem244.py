import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
# %H :앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
# %M : 앞의 빈자리를 0으로 채우는 2자리 분 숫자
# %S :앞의 빈자리를 0으로 채우는 2자리 초 숫자