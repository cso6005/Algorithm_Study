import sys
x=1
y=1
Max = -1
for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    if max(lst) > Max:
        Max = max(lst)
        x = i+1
        y = lst.index(Max)+1
print(Max)
print(x, y)

# 2
# m=(l:=sum([list(map(int,input().split()))for _ in range(9)],[])).index(a:=max(l))
# p=print
# p(a)
# p((m)//9+1,(m)%9+1)


# 3 어차피 최대값이니깐 이중배열로 넣을 필요 없음. 그냥 1차원배열에 다 넣고 max 구한 뒤, 인덱스 찾으면 됨.
import sys

arr=[]
for i in range(9):
    arr+=list(map(int,sys.stdin.readline().split()))
max=max(arr)
max_index=arr.index(max)
print(max)
print(max_index//9+1,max_index%9+1)
