def vaild(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == '[':
                if ch == ']':
                    stack.pop()
                else:
                    stack.append(ch)
            elif stack[-1] == '{':
                if ch == '}':
                    stack.pop()
                else:
                    stack.append(ch)
            elif stack[-1] == '(':
                if ch == ')':
                    stack.pop()    
                else:
                    stack.append(ch)  
    if stack:
        return False
    else:
        return True
        

def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return answer
    
    for i in range(len(s)):
        if vaild(s[i:] + s[:i]):
            answer += 1
        
    return answer