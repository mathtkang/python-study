# 상속 : 부모 클래스의 멤버를 자식 클래스에 물려주는 것
# 하나하나 만들기, 관리하기 어려우니까 공통된 부분을 묶어버린 것

class FindTen:
    def __init__(self, number):
        self.number = number

    def two(self):
        return self.number % 2

    def five(self):
        return self.number % 5


class FindSix:
    def __init__(self, number):
        self.number = number
        self.find_five = FindTen(number)

    def two(self):
        return self.number % 2

    def three(self):
        return self.number % 3

    def five(self):
        return self.find_five.five()
