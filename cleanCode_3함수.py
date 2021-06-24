# 함수의 기능 : 하나의 함수에는 하나의 기능만 존재해야 함수만의 장점을 살리는 것
def speed_up(speed):
    speed += 10
    return speed


def print_speed(speed):
    print("차의 속도는 " + str(speed) + " 입니다.")


my_speed2 = 0
my_speed2 = speed_up(my_speed2)
print_speed(my_speed2)


# 함수의 매개변수 : 너무 많다면 코드가 잘못된 것은 아닌지 의심해봐야 함
def find_seven(num_list):
    count_seven = 0

    # 방법1
    for i in range(len(num_list)):
        if num_list[i] == 7:
            count_seven += 1

    # 방법2
    # for val in num_list:
    #     if val == 7:
    #         count_seven += 1

    # 방법3
    # for idx, val in enumerate(num_list):
    #     (0, 7), (1, 4), (2, 7) #인덱스와 값을 같이 반환

    return count_seven


find_seven([7, 4, 7])
