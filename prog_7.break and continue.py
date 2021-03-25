# break : 반복문을 종료시키는 기능
# continue : 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능

list = [1, 2, 3, 5, 7, 2, 5, 237, 55]

for val in list:
    if val % 3 == 0:
        print(val)  # list안에 있는 값중 해당 조건을 만족하는 모든 값 출력
        break  # 하나의 값만 출력되고 반복문 종료

for i in range(10):
    if i % 2 != 0:
        print(i)
        print(i)
        print(i)
        print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # 를 사용하는 이유 : 중요한 코드가 더 깊은 블록으로 들어가는 것을 방지하기 위해서
    print(i)
    print(i)
    print(i)
    print(i)
