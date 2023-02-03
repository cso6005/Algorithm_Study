
# Counter 사용으로 시간 초과 해결
from sys import stdin
from collections import Counter

N = int(stdin.readline().strip())
lst = [int(stdin.readline().strip()) for _ in range(N) ]

if len(lst)==1:
    print(lst[0])
    print(lst[0])
    print(lst[0])
    print(0)
else:
    lst.sort() # 먼저 오름차순으로 정렬하고 Counter 에 넣으면 같은 빈도값이 있을 때 그들은 오름차순으로 결과가 나올 것
    val = Counter(lst).most_common(2) # 빈도 체크. 
    
    print(round((sum(lst)/N)))
    print(sorted(lst)[N//2])  

    if len(val) == 1:
        print(val[0][0])
    else:
        if val[0][1] == val[1][1]:
            print(val[1][0])
        else:
            print(val[0][0])

    print(max(lst)-min(lst))




# 시간 초과 # => .count() 오래걸림.

# if len(lst)==1:
#     print(lst[0])
#     print(lst[0])
#     print(lst[0])
#     print(0)
# else:
#     val = []
#     cnt = 0
#     for i in set(lst):
#         if lst.count(i) > cnt:
#             val, cnt = [i], lst.count(i)
#         elif lst.count(i) == cnt:
#             val.append(i)
    
#     print(round((sum(lst)/N)))
#     print(sorted(lst)[N//2])
#     if len(val) == 1:
#         print(val[0])
#     else:
#         print(sorted(val)[1])
#     print(max(lst)-min(lst))



    # c = [[i, lst.count(i)] for i in set(lst)]
    # c =sorted(c, key=lambda x:(x[1], -x[0]))






    # if c[-1][1] == c[-2][1]:
    #     print(c[-2][0])
    # else:
    #     print(c[-1][0])
        

    # lst1 = sorted(lst, key=(lst.count))




