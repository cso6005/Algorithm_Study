from sys import stdin

lst = []
leng = 0
for _ in range(5):
    a = stdin.readline().strip()
    leng = max(leng, len(a))
    lst.append(a)

result = [[] for _ in range(leng)]

for i in range(5):
    for j in range(len(lst[i])):
        result[j].append(lst[i][j])
for idx in range(leng):
    print( *result[idx], end='', sep='')


# 다른 풀이
x=['']*75
i=0

while i<5:
 j=0
 s=input()

 while j<len(s):
    x[j*5 + i] = s[j]
    j+=1
 i+=1

print("".join(x))