h, m = map(int, input().split())
time = int(input())

m = m + time
plush = int(m / 60)
plusm = int(m % 60)
h = h + plush
if h >= 24:
    h = h - 24
print(str(h) + ' ' + str(plusm))