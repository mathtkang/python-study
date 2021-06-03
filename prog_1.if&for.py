# if문 예제
age = 80
if age >= 60:
    print('고령')
    # return ~~
elif age < 60 or age >= 20:  # else if 를 줄여서 elif 로 사용
    print('성인')
else:  # age < 20 인 경우
    print('청소년')

# 파이썬에서는 논리연산자(||, &&)를 사용할 수 없다
# 대신에 or, and 를 사용! 주의!!

# 파이썬에서는 ==를 두번 연속해서 사용가능
if a == b == c:
    print(a)

# for문, 딕셔너리 같이 사용
ages = {
    'Tod': 35,
    'Jane': 23,
    'Paul': 62
}

# key : 객체의 속성 / value : 객체의 속성값

for key in ages.keys():
    # for key in ages: 키는 그대로 출력됨
    print(key)

for value in ages.values():
    print(value)

for key in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
