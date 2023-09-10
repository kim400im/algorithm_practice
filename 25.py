N, M = map(int, input().split())
list = []
for i in range(N):
    list.append(i)
for i in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        list[i] = c
for i in range(N):
    print(list[i], end=" ")