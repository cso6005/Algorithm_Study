from sys import stdin

def pseudo_palindrom_check(left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False # 유사 회문도 안 됨.
    return True # 유사회문

def palindrom_check(left, right):
    while left < right:
        if word[left] == word[right]:
            left+=1
            right-=1
        else:
            if pseudo_palindrom_check(left, right-1) or pseudo_palindrom_check(left+1, right):
                return 1 # 유사회문
            return 2 # 둘 다 아님.
    return 0 # 회문

for _ in range(int(stdin.readline().strip())):
    word = stdin.readline().strip()
    n = len(word)
    # left 제일 앞 인덱스와 right 제일 끝 인덱스 로 두 포인터 잡음. 이들의 값을 바꿔가며 회문을 확인 할 것이다.
    print(palindrom_check(0, len(word)-1)) 
