N = int(input())
for i in range(1, N+1):
    n = ' '*(N-i)
    m = '*'*i
    print(n+m)

# for in 문을 돌려 각각 출력하고 싶을 때. 아래 처럼 하면 됨!!
[print(' '*(N-i)+'*'*i) for i in range(1,N+1)]