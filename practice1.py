# 자료형

# 숫자형
print(5)
print(1+1)
print(3-2)
print(5*2)
print(6/3)  # 2.0 (나누기계산) (실수자리로 출력)
print(2**3)  # 2^3 = 8 (제곱계산)
print(5 % 3)  # 2 (나머지 출력)
print(10//3)  # 3 (몫만 출력)

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

# 숫자인 경우
# +로 연결할때는 str()으로 감싸줘야하고, 그냥 연결할 때는 ','로 해줌
print("우리집 " + animal + " 이름은 " + name)
print(name + "는 " + str(age) + "살이고, " + hobby + "을 좋아한다")
print(name, "는 ", age, "살이고, ", hobby, "을 좋아한다")
# + 외에도 , 로도 연결해서 출력할 수 있다 (이때 띄어쓰기는 자동포함)
print(name + "는 어른인가? " + str(is_adult))
