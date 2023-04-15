def vaild(s):
    cnt = 0
    while True:
        if s == '':
            return True
        
        if '{}' not in s and '[]' not in s and '()' not in s:
            return False
        
        if '{}' in s:
            s = ''.join(s.split('{}'))
        elif '[]' in s:
            s = ''.join(s.split('[]'))
        elif '()' in s:
            s = ''.join(s.split('()'))
        
        

def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return answer
    
    for i in range(len(s)):
        if vaild(s[i:] + s[:i]):
            answer += 1
        
    return answer