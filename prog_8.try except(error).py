# 주로 생기는 오류

# 1.자료형 반환 오류
text = 'abc'
number = int(text)  # ValueError: invalid literal for int() with base 10: 'abc'
# abc는 문자형에서 숫자형으로 바꿀 수 없다!

# 2.색인오류
list = []
list[0]  # IndexError: list index out of range


try:
    #     에러가 발생할 가능성이 있는 코드
except Exception:
    #     ~~과 같은 에러가 발생 시 출력되는 코드

    # 기존 코드는 애러가 나면 그 이후 코드는 읽지 않는다.
    # BUT 'try except 구문'은 해당코드 이후도 읽는다.

    # 경우 1) ValueError
text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))


# 경우 2) IndexError / if-else문으로 치환가능
def safe_pop_print(list, index):
    # try:
    if index < len(list):
        print(list.pop(index))
    # except IndexError:
    else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))


safe_pop_print([1, 2, 3], 5)


# 경우 3) ImportError
try:
    import my_module
except ImportError:
    print("모듈이 없습니다.")
