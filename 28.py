list = []
count = 0
for i in range(10):
    n = int(input())
    k = n % 42
    
    if k in list:
        pass
    else:
        list.append(k)
        count += 1
print(count)