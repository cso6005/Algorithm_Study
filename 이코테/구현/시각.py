# 이코테 p.113
N = int(input())
c = 0
for i in range(0, N+1):
    for j in range(0, 60):
        for r in range(0, 60):
            s = str(i)+str(j)+str(r)
            if '3' in s:
                c+=1
print(c)

