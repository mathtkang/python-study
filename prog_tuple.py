list1 = [1, 2, 3]
# 튜플 선언
tuple1 = (1, 2, 3)
tuple2 = 4, 5, 6

list2 = [3, 4, 5]
tuple3 = tuple(list2)

print(list1)
print(tuple1)
print(tuple2)
print(list2)
print(tuple3)
print(tuple3[0])  # 3 :값을 읽는건 가능!

# list는 변경 및 삭제 가능
list1[0] = 0
print(list1)  # [0, 2, 3]
del(list2[0])
print(list2)  # [4, 5]
list2.pop(0)
print(list2)

# tuple은 변경 및 삭제 '불가능'
# tuple1[0] = 0
# del(tuple1[0])
# tuple1.pop(0)
