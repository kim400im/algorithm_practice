X = []
for i in range(9):
    a = int(input())
    X.append(a)
max = X[0]
where = 1
for i in range(1,9):
    if X[i] > max:
        max = X[i]
        where = i + 1
    
print(str(max))
print(str(where))