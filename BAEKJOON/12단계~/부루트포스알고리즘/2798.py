from sys import stdin
N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
min = -1

for i in range(N):
    for j in range(N):
        for r in range(N):
            if i!=j and j!=r and i!=r:
                result = nums[i]+nums[j]+nums[r]
                if result <= M:
                    if min < result:
                        min = result
print(min)

