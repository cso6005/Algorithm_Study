
#Q5.

# 풀기
def solution(s):
    result = True
    S = s.upper()

    if S.count("P") != S.count("Y"):
        result = False 
    
    return result

# 최상
def solution(s):

    return s.lower().count('p') == s.lower().count('y')


#Q6. //
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

# 최상
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]


    


