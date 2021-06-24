# [원 넓이 구하기]
# main.py 에는 원의 넓이를 반환하고 출력하는 get_circle_area() 함수와 그 함수를 테스트하는 코드가 있습니다.
# 작성된 코드를 지시사항에 따라 클린 코드로 수정해보세요.

# [지시사항]
# 1. get_circle_area() 함수를 원의 넓이를 출력하는 print_area() 함수와 원의 넓이를 반환하는 get_area() 함수로 분리하세요.
# - 두 함수 모두 매개변수로 반지름(radius)를 입력받습니다.
# - print_area(3)를 호출했을 때 원의 넓이가 정상적으로 출력되도록 하세요.
# 1. 반지름 3.141592 를 math 모듈을 import하고 그 안에 있는 상수 math.pi로 수정하세요.
# 2. 중복되는 조건문을 수정하여 원의 크기가 20보다 클 때 더 큰 원입니다. 를 출력하도록 하세요.

import math


def get_area(radius):
    area = math.pi * radius * radius
    print("원의 넓이:", area)
    return area


def print_area(radius):
    if radius > 20:
        print("더 큰 원입니다.")
    elif radius > 10:
        print("큰 원입니다.")
    else:
        print("작은 원입니다.")


result = get_area(3)
print_area(result)
