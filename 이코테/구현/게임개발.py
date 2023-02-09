# 이코테 p.118

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)


# 문제 잘 못 이해함..
# 3. 모든 방향이 다 가보거나 바다일 경우 뒤로 돌아 가본 칸이라도 간다. 라는 점.
# 이동 횟수가 아니라 방문한 칸의 횟수라는 점 (3번으로 이미 가본 곳을 또 간 경우에는 count 하면 안된다.)
# => 방문한 곳을 나타내는 array 를 map 과 분리하여 만들어야 한다.

# from sys import stdin
# N, M = map(int, stdin.readline().split())
# A, B, d = map(int, stdin.readline().split())
# lst = []
# direct = [[-1, 0], [0, 1], [1, 0] , [0, -1]]
# for _ in range(N):
#     lst.append(list(stdin.readline().split())) # 문자열로 되어있음.
# result = 1
# c = 0
# while True:
#     lst[A][B] = 1
#     d -= 1    
#     if d == -1:
#         d = 3  
#     a = A + direct[d][0]
#     b = B + direct[d][1]
    
#     if lst[a][b] == '0':
#         result += 1
#         c = 0 
#         A, B = a, b
#         continue
#     else:
#         c += 1

#     if c == 4:
#         a = A + direct[d-2][0]
#         b = B + direct[d-2][1]
#         if lst[a][b] == '0':
#             result +=1
#             c = 0
#             A, B = a, b                        
#         else:
#             break
# print(result)

    



