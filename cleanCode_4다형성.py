# 다형성 : 동일한 모양의 코드가 다른 동작을 하는 것

# 객체지향프로그래밍 이라서 가능한 것
# 상속시, 변수를 각 객체에 따라서 바꿨다면
# 변수 말고 함수도 바꿀 수 없을까? 하는 생각

# 동물의 종류를 출력하는 코드
class Animal:
    species = "모르는 동물"

    def say(self):
        print(self.species + "입니다.")


class Dog(Animal):
    species = "강아지"


class Cat(Animal):
    species = "고양이"


dog = Dog()
cat = Cat()
dog.say()
cat.say()
