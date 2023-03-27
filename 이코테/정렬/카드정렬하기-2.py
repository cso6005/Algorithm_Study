import heapq
from sys import stdin
n = int(stdin.readline().strip())
heap = []
for i in range(n):
    heapq.heappush(heap, int(stdin.readline().strip())) # 아래서 오름차순 정렬되어 삽입된다.
print(heap)

result = 0
while len(heap) != 1:
    one = heapq.heappop(heap) 
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)
