# import sys
# c = 0
# for x in range(int(sys.stdin.readline().strip())):  
#     r = True
#     s = sys.stdin.readline().strip()
#     for i in s:
#         idx_lst = []
#         chr_c = s.count(i)
#         while chr_c > 0:
#             idx = s.find(i)
#             idx_lst.append(idx)
#             s = list(s)
#             s[idx:idx+1] = '-'
#             s = ''.join(s)
#             chr_c-=1
#         for i in range(len(idx_lst)-1):
#             if idx_lst[i+1] - idx_lst[i] > 1:
#                 r = False    
#     if r:
#         c+=1
# print(c)


#2


def g(a): 
    print(list(a)==sorted(a, key=a.find))
    return list(a)==sorted(a, key=a.find)

# True 나 False 를 반환. sum() 인자로 넣으면, False를 제외한 수를 셀 수 있다.!!
print(sum(g(input()) for _ in range(int(input()))))



# 3
# N = int(input())
# for i in range(N):
#     a = input()
#     print(sorted(a, key=a.find))

#     if list(a) != sorted(a, key=a.find):
#         N -= 1
# print(N)
