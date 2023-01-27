# 1 36ms
p = input().split()
p = [int(i) for i in p]

lst = [1,1,2,2,2,8]
for i in range(6):
    print(lst[i]-p[i], end=' ')

# 2 44ms
p = input().split()
p = [int(i) for i in p]
for idx, v in enumerate([1,1,2,2,2,8]):
    print(v-p[idx], end=' ')

# 3 40ms
a, b, c, d, e, f = input().split()

print(1-int(a))
print(1-int(b))
print(2-int(c))
print(2-int(d))
print(2-int(e))
print(8-int(f))