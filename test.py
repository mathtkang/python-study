# 프로그래머스 인공지능 테스트

from datetime import date
import datetime

purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
pur
for i in range(len(purchase)):
    # print(purchase[i])
    purchase[i] = purchase[i].split(' ')  # purchase.join('') #이것때문에 2차원배열로 재생성
    print(datetime.datetime.strptime(purchase[i][0], '%Y/%m/%d'))
    purchase[i][0] = datetime.datetime.strptime(purchase[i][0], '%Y/%m/%d')

print(purchase)


date = '2020/03/15'
d = datetime.datetime.strptime(date, '%Y/%m/%d')
print(d)


# ------


print('현재 시간부터 5일 뒤')
print(time2 + timedelta(days=5))  # 2018-07-28 20:58:59.666626
print('현재 시간부터 3일 전')
print(time2 + timedelta(days=-3))  # 2018-07-20 20:58:59.666626
print('현재 시간부터 1일 뒤의 2시간 전')
print(time2 + timedelta(days=1, hours=-2))  # 2018-07-24 18:58:59.666626


d0 = date(2008, 8, 18)  # date 객체1
d1 = date(2008, 9, 26)  # date 객체2
delta = d0 - d1  # 빼기
print delta.days  # 날짜로 계산
