from sys import stdin

def check(left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False # 유사 회문도 안 됨.
    return True

def twopointer(left, right):
    while left < right:
        if word[left] == word[right]:
            left+=1
            right-=1
        else:
            if check(left, right-1) or check(left+1, right):
                return 1
            return 2
    return 0

for _ in range(int(stdin.readline().strip())):
    word = stdin.readline().strip()
    n = len(word)
    print(twopointer(0, len(word)-1)) # 제일 앞 인덱스와 제일 끝 인덱스

