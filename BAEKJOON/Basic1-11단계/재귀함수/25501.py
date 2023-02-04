from sys import stdin

# def recursion(s, l, r):
    
#     if l >= r: 
#         return print(1, l+1)
#     elif s[l] != s[r]: 
#         return print(0, l+1)
#     else: 
#         return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# for _ in range(int(stdin.readline().strip())):
#     isPalindrome(stdin.readline().strip())


# 사실, 팰린드롬 판별식은 재귀함수 안쓰고, 
# 아래 코드로 간단히 가능
def isPalindrome(s):
    if s == s[::-1]:
        return 1
    return 0
