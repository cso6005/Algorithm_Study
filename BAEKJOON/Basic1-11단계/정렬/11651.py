from sys import stdin
import sys
# N = int(stdin.readline().strip())

# lst = [ list(map(int, stdin.readline().split()) ) for _ in range(N)]
# [print(*i, sep=' ' ) for i in sorted(lst, key=lambda x:(x[1], x[0]))] 
# import sys

# 2 여러 줄 한 번에 받는 걸로 readlines 사용!
# 파일 내용 전체를 가져와 리스트로 반환합니다. 
# 각 줄은 문자열 형태로 리스트의 요소로 저장

li = sys.stdin.readlines()[1:]
print(li)
li.sort(key=lambda x: int(x.split()[0]))
li.sort(key=lambda x: int(x.split()[1]))
print("".join(li))