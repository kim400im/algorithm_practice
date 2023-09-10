N = int(input())
X = list(input().split())
X = list(map(int, X))
min = X[0]
max = X[0]
for i in range(1,N):
    if X[i] < min:
        min = X[i]
    if X[i] > max :
        max = X[i]

print(str(min) + " " + str(max))

