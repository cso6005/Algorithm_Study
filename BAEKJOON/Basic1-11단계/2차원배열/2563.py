import sys
N = int(sys.stdin.readline().strip())
All = 100*N
lst = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x,x+10,y,y+10])

print(lst)

c = 0
for i in range(N):
    n = 1
    while(n<=N-1-i):
        if lst[i][1] - lst[i+n][0] >= 0: # x #같은 좌표 일수도.
            if lst[i][2] - lst[i+n][3] <=0: # y 
                print("넓이빼기")
                c+=1 # 겹쳐서 넓이 빼준 거 카운트 # 얼만큼 빼줬는 지를 저장해두고 마지막에 중복을 더하기/???
        
        n+=1

if c == N:
    print("N개 색종이가 한번에 겹치는 부분이 있어, 그 부분을 더해줘야 함.")



# lst = [[],[]]
# print(lst)

# for i in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     lst[0].append(x)
#     lst[1].append(y)
# print(lst)

