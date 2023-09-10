n = int(input())
x = list(input().split())
a = int(input())
count = 0
for i in range(n):
    if int(x[i]) == a:
        count = count + 1
print(count)
