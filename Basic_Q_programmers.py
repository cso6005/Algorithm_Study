
#Q5.

# 풀기
def solution(s):
    result = True
    S = s.upper()

    if S.count("P") != S.count("Y"):
        result = False 
    
    return result

# 다른답풀이
def solution(s):

    return s.lower().count('p') == s.lower().count('y')


#Q6. // 다른답풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a


def solution(arr):
    answer = []
    k = -1
    for i in arr:
        if i != k:
            k = i
            answer.append(i)
return answer

# Q7.

# 풀기
def solution(s):
    num = len(s)

    if num % 2 == 1:
        answer = s[num//2]
    else:
        answer = s[(num//2)-1:(num//2)+1]

    return answer

#  다른답풀이
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# Q8.

# 풀기
def solution(x, n):

    return [x*i for i in range(1,n+1)]

#Q9.
# 풀기
a, b = map(int, input().split(' '))
for i in range(b):
    print("*"*a)

# 다른답풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

#Q10.
#풀기
def solution(arr):
    return sum(arr)/len(arr)
 
# Q11.


#Q12.

#풀기
def solution(num):

    return "Even" if num%2==0 else "Odd"


#Q13.
#풀기

def solution(n):
    
    return sum([int(i) for i in str(n)])

# Q14.
# [풀기] 
# 최대공약수 : 범위 뒤부터 (공약수 중 최대이니) 동시에 약수가 되는(나누었을 때 나머지가 0)
# 최대공배수는 최대공약수로 구하기 : 최대공약수 * 최대공배수 = 두수의 곱
# if 조건, 논리연산자 괄호 잘 묶어주기
# max(a) min(a)  a -> 리스트, 튜플, 문자열(유니코드 가장 큰/작은 문자 ,문자열끼리 비교 : 가장앞부분부터 유니코드 비교)   
#    매개변수들은 크기 비교할 수 있어야 한다. 데이터 타입이 다르면 타입에러.

def solution(n, m):
    for i in range(min(n,m), 0, -1):
        if not (n % i or m % i):
            return [i, (n*m)//i]
# Q.15

# [풀기]
# 제곱근함수 math.sqrt 이용. sqrt값이 정수일 때 제곱근이라 판단
# if문 한 줄에 넣기 
"co1" if int_a > 3 else "co2")
"co1" if int_a > 3 else "co2" if int_a == 2 else "co3")


import math

def solution(n):
    return  int(pow(math.sqrt(n)+1,2)) if int(math.sqrt(n))==math.sqrt(n) else -1


#  다른 답 풀이
# [참조] 정수임을 찾는 방법 : n % 1 ==0 이면 정수
def nextSqure(n):
    from math import sqrt
    return -1 if sqrt(n) % 1 else (sqrt(n)+1)**2

# [참조] 제곱근 -> n**(1/2) 
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1


# Q.16

# [풀기]
def solution(s):

    answer = False
    if (len(s) == 4) or (len(s) == 6):
        try:
            if int(s) != 0:
                answer = True

        except(ValueError):
            pass

    return answer


# [다른답풀이_ 예외처리_ 내가 푼 것 더 간단하게]

def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 


# [다른답풀이_ 예외처리, isdigit 함수]
# s.isdigit("판단할 문자열")   :   문자열이 숫자로만 이루어져있는지 확인하는 함수 boo1 반환
# "판단할 문자열".isdigit()  # 하지만 실수나 음수를 판단하지 못함. '-' '.' 판단 못함.

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


# [다른답풀이_ 정규표현식]

def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))





