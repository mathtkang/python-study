# 1. 튜플과 리스트 이용

list = [1, 2, 3, 4, 5]

# for i, v in enumerate(list):
#     print('{}번째 값 : {}'.format(i, v)

# 변수 i와 v를 a라는 튜블에 넣어준다
for a in enumerate(list):
    print('{}번째 값 : {}'.format(a[0], a[1]))
    print('{}번째 값 : {}'.format(*a))
    # 튜플 a에 대해서 '*a'의 의미는 각각의 모든 튜플 a의 값을 나눠준다!


# 2. 튜플과 딕셔너리 이용

ages = {
    'Tod': 35, 'Jane': 23, 'Paul': 62
}

for key, val in ages.items():
    print('{}의 나이는 : {}'.format(key, val))

for a in ages.items():
    print('{}의 나이는 : {}'.format(a[0], a[1]))
    print('{}의 나이는 : {}'.format(*a))
