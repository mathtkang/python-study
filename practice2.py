from random import *
from math import *

# 수식
number = 14
number /= 2
print(number)
number %= 2
print(number)

# 절댓값
print(abs(-5))  # 5
# 제곱
print(pow(4, 2))  # 4^2 = 16
# 최대, 최소
print(max(5, 12))  # 12
print(min(5, 12))  # 5
# 정수로 반올림
print(round(3.14))  # 3
print(round(4.99))  # 5

# 정수로 올림
print(floor(4.99))  # 4
# 정수로 내림
print(ceil(3.14))  # 4
# 제곱근
print(sqrt(16))  # 4

print(random())  # 0.0(이상) ~ 1.0(미만) 사이의 임의의 값 출력
print(random() * 10)  # 0.0 ~ 10.0 사이의 임의의 값 출력
# int로 감싸주면 정수만 출력
print(int(random() * 10))  # 0(이상)~10(미만)의 임의의 값 출력
print(int(random() * 10) + 1)  # 1(이상)~10(이하)의 임의의 값 출력
print(int(random() * 45) + 1)  # 1(이상)~45(이하)의 임의의 값 출력
# 동일한 표현
print(randrange(1, 46))  # 1(이상)~46(미만)의 임의의 값 출력
print(randint(1, 45))  # 1과 45를 포함하는 1~45의 임의의 값 출력
