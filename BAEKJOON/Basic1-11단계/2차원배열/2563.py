n = int(input())
# 최대 범위 100인 판을 먼저 깔아두자.
back = [[0] * 100 for _ in range(100)]
 
for _ in range(n):
    a, b = map(int, input().split())
 
    # 어차피 넓이를 구하는 거니깐 인덱스 조정 안 해도 됨.
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            back[i][j] = 1 # 중요 !!
 
area = 0
for x in back:
    area += sum(x)
 
print(area)




# 100 * n) - 색종이끼리 겹치는 넓이 로 풀려고 했는데 이러면 아주아주 복잡하다.

# import sys
# N = int(sys.stdin.readline().strip())
# A = 100*N
# lst = []

# for i in range(N):
#     # x, y = map(int, sys.stdin.readline().split())
#     # lst.append([x,x+10,y,y+10])
#     lst.append(list(map(int, sys.stdin.readline().split())))


# print(lst)

# c = 0
# for i in range(N):
#     n = 1
#     dA = 0
#     while(n<=N-1-i):
#         print('---', n, lst[i], lst[i+n])

#         x, y = lst[i][0], lst[i][1]
#         x1, y1 = lst[i+n][0], lst[i+n][1]
        
#         dx = 10 
#         if x < x1:
#             dx = (x + 10) - x1
#         elif x > x1:
#             dx = (x1 + 10) - x
#         else:
#             print("완전히 겹침")
               
#         print("dx:", dx)

#         if dx > 0: 

#             dy = 10
#             if y > y1:
#                 dy = (y1+10)-y

#             elif y <y1:
#                 dy= (y+10)-y1
#             print(dy)

#             if dy > 0: # y 
#                 dA = dx * dy
#                 print(dA)
#                 c+=1 # 겹쳐서 넓이 빼준 거 카운트 # 얼만큼 빼줬는 지를 저장해두고 마지막에 중복을 더하기/???
#         n+=1

#     A -=dA
        

# if c == N:
#     print("N개 색종이가 한번에 겹치는 부분이 있어, 그 부분을 더해줘야 함.")

# print(A)

# lst = [[],[]]
# print(lst)

# for i in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     lst[0].append(x)
#     lst[1].append(y)
# print(lst)

