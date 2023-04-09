number = 123
x = 123

# 1 문자열로 변환 후, 분리하는 방법
a = []
for i in str(number):
    a.append(i)
print(a)

# 2 10으로 나누어 자릿수 분리하기(10으로 나누기때문에, 1의 자리부터 분리)
a = []
while(number!=0):
    a.append(number%10)
    number = number//10
print(a)

# 3 map 사용
lst = list(map(int, str(x)))
print(lst)

# 각 자리수 더하기
n_sum = sum(map(int, str(x)))
print(n_sum)


