n = int(input())
string = []
list = []
for i in range(n):
    string = str(input())
    str_len = len(string)
    string_is = string[0] + string[str_len - 1]
    list.append(string_is)
for i in range(n):
    print(list[i])

# import sys
# list = []
# N = int(sys.stdin.readline())
# for i in range(N):
#     a = str(input())
#     if len(a)==1:
#         list.append(a[0])
#     else:
#         list.append(a[0] + a[-1])
   

# for i in range(N):
#     print(list[i])
