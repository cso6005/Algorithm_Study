from sys import stdin
from collections import defaultdict
t = int(stdin.readline().strip())
for _ in range(t):
    w = stdin.readline().strip()
    k = int(stdin.readline().strip())
    n = len(w)
    ans1 = n+1
    ans2 = -1

    alpha =  defaultdict(list)
    for i in range(n):
        if w.count(w[i]) >= k:
            alpha[w[i]].append(i)
    if not len(alpha):
        print(-1)
        continue

    for val in alpha.values():
        ans1 = min(ans1, val[k-1]-val[0]+1)
        ans2 = max(ans2, val[k-1]-val[0]+1)

        if len(val) > k:
            for j in range(k, len(val)):
                ans1 = min(ans1, val[j]-val[j-k+1]+1)
                ans2 = max(ans2, val[j]-val[j-k+1]+1)
    print(ans1, ans2)
    
