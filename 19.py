n1 = []
n2 = []
sum = []
count = 0
while(True):
    a, b = map(int, input().split())
    if a + b == 0:
        break
    n1.append(a)
    n2.append(b)
    sum.append(a + b)
    count = count + 1
for i in range(count):
    print(sum[i])
