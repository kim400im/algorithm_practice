import sys
t = []
a = int(sys.stdin.readline())
for i in range(a):
    x, y = map(int, sys.stdin.readline().split())
    sum = x + y
    t.append(sum)
for i in range(a):
    print(t[i])
