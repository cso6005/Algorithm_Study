from sys import stdin
from itertools import permutations

n = int(stdin.readline().strip())
A = list(map(int, stdin.readline().split()))
op = []
lst = list(map(int, stdin.readline().split()))
for i in range(4):
    for _ in range(lst[i]):
        op.append(i)
oper = list(permutations(op, n-1))

maxx = int(-10e9)
minn = int(10e9)
for opp in oper:
    val = A[0]
    for j in range(1, n):
        if opp[j-1] == 0: 
            val += A[j]
        elif opp[j-1] == 1:
            val -= A[j]
        elif opp[j-1] == 2:
            val *= A[j]
        else:
            if val < 0:
                val = -(-val//A[j])        
            else:    
                val //= A[j]
    maxx = max(val, maxx)
    minn = min(val, minn)

print(maxx)
print(minn)


    
