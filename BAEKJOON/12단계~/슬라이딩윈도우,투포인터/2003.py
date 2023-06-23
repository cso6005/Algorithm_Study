from sys import stdin

n, m = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

m_sum = 0
end = 0
cnt = 0
for start in range(n):
    while m_sum < m and end < n:
        m_sum += A[end]
        end+=1
    
    if m_sum == m:
        cnt += 1
    m_sum-=A[start]

print(cnt)
