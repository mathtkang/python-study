# 생성
list = [1, 2, 3]
dict = {'one': 1, 'two': 2}

# 호출
print(list[0])  # 1
print(dict['one'])  # 1

# 삭제
del(list[0])
del(dict['one'])

# 갯수 확인
len(list)
len(dict)

# 해당 값의 존재 유무 : boolean 으로 반환
print(2 in list)  # true
print('two' in dict.keys())  # true
print('3' in dict.values())  # false

# 전체 삭제
list.clear()
print(list)
dict.clear()
print(dict)

# 주의해야할 점 : .속성(값)으로 작성할 때는 -s 붙여주기!

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# list는 결합(+)하면 : 그대로 뒤에 값이 추가됨
print(list1+list2)  # [1,2,3,4,3,4,5,6]

dict1 = {'1': 1, '2': 2, '3': 3}
dict2 = {'1': 4, '5': 5, '6': 6}
# dictionary는 결합.update()하면 : 키의 값에 따라서 속성값이 덧씌워짐
dict1.update(dict2)
print(dict1)  # {'1': 4, '2': 2, '3': 3, '5': 5, '6': 6}
