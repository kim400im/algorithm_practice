a = int(input())
b= int(input())
n1 = int(b / 100)
n2 = int((b%100) / 10)
n3 = int(b% 10)

print(n3 * a)
print(n2 * a)
print(n1 * a)
print(a * b)