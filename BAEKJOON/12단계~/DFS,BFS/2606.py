import sys
N = int(sys.stdin.readline().strip())
lst = [ []*i for i in range(N+1)]
visited = [False] * (N+1)

for _ in range(int(sys.stdin.readline().strip())):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(n):
    cnt = 0
    for x in lst[n]:
        if not visited[x]:
            visited[x] = True   
            cnt += 1
            cnt += dfs(x)
    return cnt

result = 0
visited[1] = True

result += dfs(1)
print(result)

# 방문한 장소만을 묻는 것이니 사실 아래를 구하면 됨.
print(sum(visited)-1)


