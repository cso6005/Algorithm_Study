# 에라토스테네스의 체

import sys
max = 123456*2+1
lst = [True for _ in range(123456*2+1)]
for i in range(2, int(max**0.5)): # 루트값 이상은 범위 내 배수를 가질 수 없다.
    if lst[i]:
        for j in range(2*i, max, i): # i 자신을 제외한 자신의 배수를 서로수의 의미인 False 로 만들어준다.
            lst[j] = False # i의 배수(=j) 즉 무언가의 배수가 되는 수는 소수가 될 수 없는 수

while True:
    N = int(sys.stdin.readline().strip())
    c = 0
    if N == 0:
        exit()
    for i in range(N+1, 2*N+1):
        if lst[i]:
            c+=1
    print(c)



# https://joylee-developer.tistory.com/74

# 시간 초과
# lst = []
# for i in range(2, 246913):
#     for j in range(2, math.floor(math.sqrt(i))+1):
#         if i % j == 0:
#             break   
#     else:
#         lst.append(i)

# while True:
#     c = 0
#     n = int(sys.stdin.readline().strip())
#     if n == 0:
#         exit()
#     for i in range(n+1, 2*n+1):
#         if i in lst:
#             c+=1
#     print(c)