n = 5
m = 5
data = [1,2,3,2,5]
count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키면서 반복
for start in range(n):
    
    # 부분합이 m보다 작다면 end를 이동
    while interval_sum < m and end < n:
        # 작다면 end 옮기면서 계속 더하고
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    # 같거나, 큰 경우이니, start를 옮겨야 함.
    # 그래서 더해져 있던  start 빼주기
    interval_sum -= data[start]

print(count)