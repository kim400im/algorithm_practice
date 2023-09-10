T = int(input())
n1 = []
n2 = []
x = []
for i in range(T):
    a, b = map(int, input().split())
    x.append(a + b)
    n1.append(a)
    n2.append(b)
for i in range(T):
    print("Case #" + str(i + 1) + ": "+ str(n1[i]) + ' + '+ str(n2[i]) + ' = ' + str(x[i]))