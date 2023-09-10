h, m = map(int, input().split())

if m >= 45:
    m = m - 45
    print(str(h) + ' ' + str(m))
else:
    m = m + 60
    m = m - 45
    if h == 0:
        print("23 " + str(m))
    else:
        h = h -1
        print(str(h) + ' ' + str(m))
