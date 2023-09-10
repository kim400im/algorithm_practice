N, M  = map(int, input().split())
list = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    for k in range((j-i)//2 + 1):
        list[i-1+k],list[j-1-k] = list[j-1-k], list[i-1+k]
print(' '.join(str(n) for n in list))