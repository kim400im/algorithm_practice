N, X = map(int, input().split())
A = list(input().split())
A = list(map(int, A))
result = []
count = 0
for i in range(N):
    if A[i] < X:
        result.append(A[i])
        count += 1
for i in range(count):
    print(result[i], end=" ")