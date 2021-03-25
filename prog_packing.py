# packing: 하나의 변수에 여러 값을 넣는 것
# unpacking: 패킹된 변수에서 여러 값을 꺼내는 것

a, b = 1, 2
print(a)
print(b)

c = (3, 4)
# c = 3, 4 #자동으로 튜플 (1,2)로 인식
print(c)

d, e = c
print(d)
print(e)

f = d, e  # 같은말 f = 3, 4
print(f)

# 다른 언어에서는 두 변수의 값을 바꿀 때 임시변수(temp:temporary)가 필요하다.
x = 5
y = 10
temp = x
x = y
y = temp
print(x, y)  # 10,5

# BUT 파이썬에서는 필요 없다. 튜플을 이용하면 되니까!!
x = 5
y = 10
x, y = y, x
print(x, y)  # 10,5


# 함수의 리턴 값으로 여러 값 전달 가능
def tuple_func():
    return 1, 2


s, t = tuple_func()
print(s)
print(t)

q = tuple_func()
print(q)
