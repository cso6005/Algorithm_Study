
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

# Q 17.

# [풀기]
# 1) '구분자'.join(리스트) : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 하수
# ''.join(리스트) 홀따옴표 안에 아무것도 안 넣으면 그냥 합쳐서 abc 반환
# '-'.join(리스트) 'a-b-c'

# 2) sort() 함수는 str형 사용 못함
# 그래서 sorted() 를 사용. sorted(정렬할 데이터[, key 파라미터][,reverse 파라미터])
# 매개변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어서 반환해주는 함수.
# 첫 번째 매개변수로 들어올 "정렬할 데이터"는 iterable 한 데이터 이어야 합니다.
# 기본값 오름차순.    reverse=True 내림차순

# 리스트.sort()와 sorted(리스트)의 가장 큰 차이는 
#  리스트.sort() 는 본체의 리스트를 정렬해서 변환하는 것이고, str 형 안됨.
#  sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.

def solution(n):

    return int(''.join(sorted(str(n),reverse=True)))



# [다른 풀이] _ 리스트로 변환해서 sort()함수사용. 
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

# Q 18.

# [풀기]
def solution(n):

    return [int(i) for i in str(n)[::-1]]


# [다른 풀이]_ map함수()
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


# Q.19.

# [풀기]
def solution(phone_number):
    
    return ("*"*(len(phone_number)-4)) + (phone_number[len(phone_number)-4:])

# 길이를 모르는 문자열에서 뒤에서 4번째 문자를 조회하고 싶다고 할 때 
# 굳이 len()함수써서 -4 해서 할 필요없다.! 그냥 s[-4] 하면 뒤에서부터 조회!

# [다른 풀이]
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

#.20.

# [나 풀기 1 ]
def solution(array, commands):
    lst=[]
    for i in commands:
        a = array[i[0]-1:i[1]]
        a.sort()
        lst.append(a[i[2]-1])
    return lst

# [나 풀기 2]
def solution(array, commands):

    return [ sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands ]

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])


# [다른 풀이]wow

def solution(array, commands):

    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# Q. 21.

# [내가 푼 것]
# 어차피 A == 0 이런 비교연산자의 반환값은 bool 이므로 return에 바로 넣어주면 됨! 
# 굳이 if 문 안 쓰고!

def solution(x):

    if x % sum([int(i) for i in str(x)]) == 0:
        return True 
    else:    
        return False

# [다른 풀이]
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# Q. 22 
[내가 푼 것]
def solution(arr, divisor):

    a = [i for i in sorted(arr) if i % divisor == 0 ]
    if a != []:
        return a
    return [-1]

# [다른 풀이]
# 리스트 값이 있으면 True, 없으면 False !!!!
# python은 or 앞이 참일경우 해당 값까지만 , 거짓일경우 뒤에 것까지 호출
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

