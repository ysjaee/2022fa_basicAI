'''
한국대학교의 김한국교수님은 학생들과 친해지기 위해서 딸에게 줄임말을 배우기로 했습니다.
딸은 '복잡한 세상 편하게 살자' 라는 문장을 '복세편살'로 줄여 말합니다.

교수님이 줄임말을 배우기 위해 위와 같이 어떤 입력이 주어지면 앞 글자만 줄여 출력하도록 해주세요.

'''

ser_input = input().split(' ')
#print(user_input)
result = ''

for s in user_input:
    result += s[0]

print(result)