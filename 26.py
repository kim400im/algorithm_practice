N, M  = map(int, input().split())
list = []
for i in range(N):
    list.append(i + 1)
for t in range(M):
    i, j = map(int, input().split())
    temp = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = temp
for i in range(N):
    print(list[i], end=" ")