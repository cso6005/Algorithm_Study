N , X = map(int, input().split())
A = list(map(int, input().split()))
[print(i, end=' ') for i in A if i < X]


# 다른 풀이 # join 함수 이용
# 리스트의 각 원소로 이뤄진 문자열로 만드는 함수
# .join([]) => 매개변수로 들어온 리스트의 원소를 문자열로 합쳐서 반환
# '구분자'.join([]) => 리스트의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 합쳐줌.
n, x = map(int, input().split())
answer = ' '.join([i for i in input().split() if int(i) < x])
# print(type(answer)) # str
print(answer)

