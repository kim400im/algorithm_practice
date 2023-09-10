a = int(input())
t = []
for i in range(a):
    k, j = map(int, input().split())
    t.append(k + j)
for i in range(a):
    print(t[i])