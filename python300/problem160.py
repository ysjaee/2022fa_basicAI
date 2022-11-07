리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(변수)