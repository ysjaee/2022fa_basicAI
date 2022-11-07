 # 순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다. 주어진 숫자들 중 최댓값을 반환하라.


data = list(map(int, input().split()))
print(sorted(data)[-1])