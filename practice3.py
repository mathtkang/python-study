# 문자열

sentence = '나는 스갱입니다.'
print(sentence)
sentence2 = '파이썬은 쉬워요.'
print(sentence2)
sentence3 = """
나는 스갱이고,
파이썬은 완전 쉬워요!
"""
print(sentence3)

sgaeng = "971124-2345678"
# 문자열을 배열로 보고 원하는 index만 출력
print("성별 : " + sgaeng[7])
print("연도 : " + sgaeng[0:2])  # 0부터 2직전까지 출력 (즉, 0~1번째)
print("월 : " + sgaeng[2:4])
print("일 : " + sgaeng[4:6])

print("생년월일 : " + sgaeng[0:6])
print("생년월일 : " + sgaeng[:6])  # 시작하는 수 없이 : 부터 시작하면 자동 0부터!
print("주민 뒷자리 : " + sgaeng[7:14])
print("주민 뒷자리 : " + sgaeng[7:])  # 7부터 끝까지

# 맨 뒤에 있는 index를 기준으로 '끝에서 몇 번째 까지'의 숫자 출력!
print("뒤에서부터 7개 출력 : " + sgaeng[-7:])  # 맨 마지막의 숫자를 -1로 보고, 왼쪽으로 세준다.

python = "Python is Amazing"
# 모든 문자열을 소문자로 바꿈
print(python.lower())
# 모든 문자열을 대문자로 바꿈
print(python.upper())
# 해당 문자가 대문자라면 true, 소문자라면 false
print(python[0].isupper())
# 해당 문자가 소문자라면 true, 대문자라면 false
print(python[0].islower())
# 해당문자열의 길이
print(len(python))
# 앞의 문자열을 뒤의 문자열로 변환
print(python.replace("Python", "Node.JS"))

# 전체 문자열에서 n이 몇 번째에 있는지 검색
print(python.index("n"))  # 맨 앞 만
print(python.find("n"))  # 동일한 말
index = python.index("n")
print(python.index("n", index + 1))  # 해당 숫자(index+1) 뒤에서부터 검색

print(python.find("NodeJS"))  # find : 찾는 문자가 없을 때 -1 출력 (뒤의 코드 출력가능)
# print(python.index("NodeJS"))  # index : 오류 (뒤의 코드 안 읽음)
# 해당 문자가 총 몇 번 등장하는지 갯수
print(python.count("n"))
