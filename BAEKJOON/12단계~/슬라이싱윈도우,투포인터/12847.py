from sys import stdin

n, m = map(int, stdin.readline().split())
T = list(map(int, stdin.readline().split()))

m_sum = sum(T[:m])
answer = m_sum

for idx in range(m,n):
    m_sum += T[idx]-T[idx-m]
    answer = max(answer, m_sum)
print(answer)

