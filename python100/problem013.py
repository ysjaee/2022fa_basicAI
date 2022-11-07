'''
우리 태양계를 이루고 있는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성으로 총 8개 입니다. 저희는 우리 태양계의 n번째 행성이 무엇인지 알고 싶습니다.

입력으로 행성의 순서를 나타내는 숫자 n이 입력됩니다. 예를들어 수성은 첫번째 행성입니다.

```python
1
```

출력으로 그 순서에 해당하는 행성의 이름을 출력해 주세요.
1
수성
'''

planets = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

n = int(input()) - 1
print(planets[n])