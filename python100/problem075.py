'''
369 게임을 하는데 조금 이상한 규칙이 있습니다. 3이나 6, 9 일 때만 박수를 쳐야합니다. 예를 들어 13, 16과 같이 3과 6, 9 만으로 된 숫자가 아닐 경우엔 박수를 치지 않습니다.
수현이는 박수를 몇 번 쳤는지 확인하고 싶습니다. 36일 때 박수를 쳤다면 박수를 친 횟수는 5번입니다.

n을 입력하면 박수를 몇 번 쳤는지 그 숫자를 출력해주세요.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9287d7e8-16a9-43a1-bf51-e7a585b884bc/_2019-10-07__2.01.50.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9287d7e8-16a9-43a1-bf51-e7a585b884bc/_2019-10-07__2.01.50.png)

```python
**입력 - 문자로 입력받습니다.**
'93'

**출력**
10
```
'''


def sol(n):
    n = list(str(n))
    answer = 0
    count = 1
    d = {3: 1, 6: 2, 9: 3}

    while n:
        answer += d[int(n.pop())] * count
        count *= 3

    return answer