def check_and_clear(e):
    print("불량품이 있으면 box를 clear합니다.")
    if '불량품' in e.keys():
        # if '불량품' in e.keys() == True: 왜 비교연산자(==)하니까 안됨?
        e.clear()
    return print(e)


box1 = {"불량품": 10}
check_and_clear(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
