# 코딩컨벤션 : 함께 코딩하기 위한 모두와의 약속

# 잘못된 예시 : 그 상태마다 주석으로 설명하기 보다
status = 0

if status == 0:  # 숫자 0이 의미하는 바는~
    print("공격!")
elif status == 1:  # 숫자 1이 의미하는 바는~
    print("수비!")
else:
    print("대기")

# 올바른 예시
status = 0
ATTACK_STATUS = 0
DEFENCE_STATUS = 1

if status == ATTACK_STATUS:  # 직관적으로 인식할 수 있도록 상단에 상수로 정의
    print("공격!")
elif status == DEFENCE_STATUS:
    print("수비!")
else:
    print("대기")
