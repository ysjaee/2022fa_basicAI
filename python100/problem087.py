'''
천하 제일 먹기 대회가 개최되었습니다.
이 대회는 정해진 시간이 끝난 후 음식을 먹은 그릇 개수를 파악한 후 각 선수들의 등수를 매깁니다.

1. 같은 이름의 선수는 없습니다.
2. 접시의 수가 같은 경우는 없습니다.

**입력 예1)**

```python
손오공 야모챠 메지터 비콜로
70 10 55 40
```

**출력 예1)**

```python
{'손오공': 1, '메지터': 2, '비콜로': 3, '야모챠': 4}
```

**입력 예2)**

```python
["홍길동","엄석대","연개소문","김첨지"]
[2, 1, 10, 0]
```

**출력 예2)**

```python
{'연개소문': 1, '홍길동': 2, '엄석대': 3, '김첨지': 4}
```
'''

name = 'A C B D'.split(' ')
point = list(map(int, '70 10 55 40'.split(' ')))


def hojun(x):
    return x[1]


def sol(name, point):
    d = {}
    z = [[i, j] for i, j in zip(name, point)]
    z = sorted(z, key=hojun, reverse=True)

    for i in range(len(z)):
        d[z[i][0]] = i + 1
    return d


print(sol(name, point))

test = 'AA CCCC BBB D'.split(' ')
sorted(test, key=len)