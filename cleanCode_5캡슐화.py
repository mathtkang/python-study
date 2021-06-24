# 캡슐화 : 클래스를 앞으로 사용할 사람들을 위해서 내부의 복잡한 것은 감추고 필요한 것만 간단하게 사용할 수 있도록 한 것
# 클래스 내 존재하는 멤버 변수를 클래스 내 메서드를 통해서만 설정하고 반환할 수 있게 하는 것

class Human:
    def __init__(self, name, birthday):
        self.__set(name, birthday)

    def __set(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    # 아래 두 경우로 나눈 이유 : 함부로 접근하지 못하도록
    def get_name(self):
        return self.__name

    def get_birthday(self):
        return self.__birthday

# 접근제한자 : 밖에서 저 원소에서 접근할 수 없도록 앞에 __언더바를 사용 (java private와 비슷)
