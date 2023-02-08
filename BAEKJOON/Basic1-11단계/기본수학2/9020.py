# 소수 문제
import sys

# 입력 받을 때마다 반복문 도는 것보다는 먼저 범위 내 소수를 찾자.
check = [False, False] + [True] * 10000 # 0,1 제외 일단 다 소수
for i in range(2, 101):
    if check[i] == True:
        for j in range(2*i, 10001, i):
            check[j] = False

# 입력 받기 시작.
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    A = n // 2 # 입력의 중간값부터 탐색
    B = A
    while True:
        if check[A] and check[B]: # 둘 다 소수일 때
            print(A, B)
            break
        A -= 1 # 중간을 기점으로 +1 -1 씩 한 값들의 합은 n 으로 같다.
        B += 1








# import sys
# import math

# for _ in range(int(sys.stdin.readline().strip())):
#     n = int(sys.stdin.readline().strip())
#     lst = []
#     for i in range(2, 2*(n-1)+1 ):
#         for j in range(2, math.floor(math.sqrt(i))+1):
#             if i % j == 0:
#                 break
#         else:
#             print("소수", i)
#             lst.append(i)
    
#     print(lst)

#     for x in lst:
#         if (n - x) in lst:
#             print(x, n-x)
#             break