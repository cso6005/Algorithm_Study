from sys import stdin
n = int(stdin.readline().strip())
cow = [-1]*11
move = []
[move.append(list(map(int,stdin.readline().split()))) for _ in range(n)]
cnt = 0
for m in move:
    if cow[m[0]] == -1:
        cow[m[0]] = m[1]
    else:
        if cow[m[0]] != m[1]:
            cow[m[0]] = m[1]
            cnt+=1
print(cnt)