# 약수 구하기
div = int(input())
list1 = []
for i in range(div, 0, -1):
    if div % i == 0:
        list1.append(div//i)
print(list1)

# In the Middle
num1 = int(input())
num2 = int(input())
num3 = int(input())

list1 = [num1, num2, num3]
list1.sort()
print(list1[1])
