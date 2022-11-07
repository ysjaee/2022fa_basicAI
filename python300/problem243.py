import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    before_day = datetime.timedelta(days=day)
    date = now - before_day
    print(date)