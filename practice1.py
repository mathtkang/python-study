# 자료형

# 숫자형
print(5)

# 문자열
print('풍선')
print('a'*5)

# boolean
print(5 > 10)
print(True)
print(not True)
print(not (5 > 10))

# 변수
animal = "강아지"
name = "뽀미"
age = 4
# 숫자형,불린형(문자열이 아닌데, print로) 출력시 : str()로 감싸준다
hobby = "산책"
is_adult = age >= 3  # 불린형태

print("우리집 강아지 이름은 뽀미")
print("뽀미는 4살이고, 산책을 좋아한다")
print("뽀미는 어른인가? true")

print("우리집 " + animal + " 이름은 " + name)
print(name + "는 " + str(age) + "살이고, " + hobby + "을 좋아한다")
print(name, "는 ", age, "살이고, ", hobby, "을 좋아한다")
# + 외에도 , 로도 연결해서 출력할 수 있다 (이때 띄어쓰기는 자동포함)
print(name + "는 어른인가? " + str(is_adult))
