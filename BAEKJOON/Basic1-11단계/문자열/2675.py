import sys
for _ in range(int(sys.stdin.readline().strip())):
    S = sys.stdin.readline().strip()
    print(''.join(list(map(lambda x: x*int(S[0]) , S[2:]))))

# 2
# 어차피 2 abc 이렇게 공백을 두고 들어오니 split 으로 받아도 됨.
# n,s=input().split()
t=int(input())
for _ in range(t):
    n,s=input().split()
    for i in s:
        print(i*int(n),end="")
    print()