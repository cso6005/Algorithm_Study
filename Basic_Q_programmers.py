
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


