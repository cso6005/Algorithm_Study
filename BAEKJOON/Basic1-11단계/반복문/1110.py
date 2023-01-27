c = 0
N = input()
X = N

while int(X)!=int(N) or c == 0:
    s = sum(map(int, X))
    X = X[-1] + str(s)[-1]
    c+=1    

print(c)

# 다른 풀이
# 숫자 각자리수 분리를 //10 몫연산, %10 나머지 연산으로 해결한 풀이
N = int(input())
a = N//10
b = N%10
i=0

while True:
    c = b*10 + (a+b)%10
    a = c//10
    b = c%10
    i+=1
    if c==N:
        break
    else:
        continue
print(i)