a = int(input())
n = int(input())
sum = 0
for i in range(n):
    price, num = map(int, input().split())
    sum = sum + price * num
if sum == a:
    print("Yes")
else:
    print("No")