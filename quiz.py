from random import *

# quiz1) 변수를 이용해서 다음 문장을 출력하시오
station1 = "사당"
station2 = "신도림"
station3 = "인천공항"

# 출력 문장
print(station1, "행 열차가 들어오고 있습니다.")
print(station2, "행 열차가 들어오고 있습니다.")
print(station3, "행 열차가 들어오고 있습니다.")

# quiz2) 스터디 모임 날짜 정하기
# 월 4회 스터디, 3번 온라인, 1번 오프라인
# 조건) 랜덤으로 날짜 뽑음, 1-3일은 스터디 준비해야해서 제외, 최대 28일 이내로 지정

print("온라인1 날짜 : ", randint(4, 28))
print("온라인2 날짜 : " + str(randint(4, 28)))
print("온라인3 날짜 : ", randint(4, 28))
print("오프라인 날짜 : ", randint(4, 28))
