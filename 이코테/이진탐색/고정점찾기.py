from sys import stdin
N = int(stdin.readline().strip())
array = list(map(int, stdin.readline().split()))
result = -1
start = 0
end = N-1

# 이진탐색 방법
while start <= end:
    min = (start + end)//2
    if array[min] < min:
        start = min+1
    elif array[min] > min:
        end = min-1
    else:
        result = min
        break
print(result)




# 선형 탐색 방법
# for v in range(len(array)):
#     if array[v] == v:
#         result = v
#         break
# print(result)


