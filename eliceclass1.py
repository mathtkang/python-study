# 1.로켓발사
from math import gcd
count = 10
list = range(count, 0, -1)
for i in list:
    print(i)


# 2.개굴개굴개구리
# 정답
a = input()
for i in a:  # a = "안녕 나는 엘리스야"
    if i == " ":
        print(" ", end="")
    else:
        print("개굴", end="")

# 내가 작성한 답
string = input()
# list1 = string.split( )
# print(list1) # ['안녕', '나는', '엘리스야']
result = ""
for i in string:  # string그 자체가 문자열(시퀀스)
    if i == " ":
        result += " "
    else:
        result += "개굴"
print(result)


# 3.계단오르기
def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)  # 5

    while (current < n):
        current += steps[cnt]
        cnt += 1
    return cnt


print(crossBridge([1, 1, 2, 3, 5]))


# 4.문자열에서 "F"로 시작하는 단어 찾기
def isPrince(frogList):
    # print(frogList[0][2])
    for i in frogList:
        if i[0] == 'F':  # frogList[i][0] 이게 왜 안되지? > 매개변수 i자체에 frogList[0] 부터 차례로 들어간다는 의미
            return i


print(isPrince(['Alice', 'Bob', 'Frog']))


# 5.토끼와 거북이의 달리기 경주
def lcm(x, y):
    return x * y // gcd(x, y)


N, M = input().split()
N = int(N)  # 3
M = int(M)  # 5

print(lcm(N, M))

# # rabbit = [N*1,N*2,N*3, ...]
# # turtle = [M*1,M*2,M*3, ...]
# rabbit = list(range(N,100,N))
# turtle = list(range(M,100,M))
# for i in rabbit :
#     for j in turtle :
#         if i == j :
#             print(i)
#             break;


# 6.엘리스와 별헤는 밤
num = int(input())
star = "*"
interval = " "
result1 = star + interval*num + star + interval*num + star
if num % 2 == 0:
    result2 = interval*(num-(num-1)//2) + star + interval*(num-1) + star
else:
    result2 = interval*(num//2+1) + star + interval*num + star
print(result1)
print(result2)
