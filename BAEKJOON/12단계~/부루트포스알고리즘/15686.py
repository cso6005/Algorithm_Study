from sys import stdin
from itertools import combinations, permutations

n, m = map(int, stdin.readline().split())
city = []
chic = []
home = []
[city.append(list(map(int, stdin.readline().split())))for _ in range(n)]



for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chic.append((i, j))
        elif city[i][j] == 1:
            home.append((i,j))
result = int(10e9)
city_dist = 0
combi = list(combinations(chic, m))
cnt = 0
if combi != [()]: 
    for lst in combi:
        city_dist = 0
        for xx,yy in home:
            dist = int(10e9)
            for x,y in chic:
                if (x,y) in lst:
                    cnt+=1
                    dist = min(dist, abs(xx-x) + abs(yy-y))
            city_dist+=dist
        result = min(result, city_dist)


else:
    for xx,yy in home:
        dist = int(10e9)
        for x,y in chic:
            dist = min(dist, abs(xx-x) + abs(yy-y))
        city_dist +=dist
    result = city_dist
        
print(result)
