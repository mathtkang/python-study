selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요 > ')

print('선택한 값은 : ', selected)


# for문과 while문의 동일표현
patterns = ['가위', '바위', '보']

for i in range(len(patterns)):
    print(patterns[i])

length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i += 1
# 파이썬에서는 ++i, --i 같은 증감연산자를 사용하지 않음
