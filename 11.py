a, b, c = map(int, input().split())
if (a == b == c):
    prize = 10000 + a * 1000
elif (a != b) and (a != c) and (b != c):
    max = a
    if max < b:
        max = b
        if max < c:
            max = c
    else:
        if max < c:
            max = c
    prize = 100 * max
else:
    if a == b:
        prize = 1000 + 100 * a
    elif a == c:
        prize = 1000 + 100 * c
    else:
        prize = 1000 + 100 * b

print(str(prize))