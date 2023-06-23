from sys import stdin

n, x = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))

sum_x = sum(lst[:x])
answer1 = sum_x
answer2 = 1

for idx in range(x,n):
    sum_x += lst[idx] - lst[idx-x]
    if answer1 < sum_x:
        answer1 = sum_x
        answer2 = 1
    elif answer1 == sum_x:
        answer2 +=1

if not answer1:
    print("SAD")
else:
    print(answer1)
    print(answer2)

