
# x = int(input())
# y_lst = list(map(int, input()))
# a = x*y_lst[2]
# b = x*y_lst[1]
# c = x*y_lst[0]
# sum = a + 10*b + c*100
# print(a)
# print(b)
# print(c)
# print(sum)

a, b = int(input()), input()
print( *[a*int(p) for p in b][::-1], a*int(b))
