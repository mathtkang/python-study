# 잘못된 예시
if x > 0:
    print("x는 자연수")
elif x == 1:
    print("x는 1")
else:
    print("x는 1보다 작은 수")

# 올바른 예시
if x > 0:
    print("x는 자연수")

if x == 1:
    print("x는 1")
else:
    print("x는 1보다 작은 수")


# 잘못된 예시
if point >= 88:
    print("A+")
elif point >= 77 and point < 88:  # 굳이 안써줘도 되는 부분
    print("A0")
elif point == 0:
    print("F")
else:
    print("B+")

# 올바른 예시
if point >= 88:
    print("A+")
elif point >= 77:  # 위에서 88미만인건 걸러서 내려오니까
    print("A0")
elif point == 0:
    print("F")
else:
    print("B+")
