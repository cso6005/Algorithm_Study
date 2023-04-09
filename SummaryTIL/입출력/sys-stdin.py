'''https://seill.tistory.com/314
Python 파일 오픈
파일 모드는 읽기 모드 ('r'), 새로 쓰기 모드 ('w'), 이어 쓰기 모드 ('a')가 있고,

 

'r'은 읽기 전용으로 파일을 오픈합니다. 읽기만 가능하고, 쓰기는 되지 않습니다.

'w' 는 쓰기 모드인데, 파일을 새로 만듭니다. 즉, 동일한 이름의 파일이 있으면 지우고 새로 작성합니다.

'a' 는 쓰기 모드인데, 'w' 와는 다르게 기존 파일에 내용을 이어서 작성합니다.


'''

f = open('경로', '모드')
f = open('/home/python/test.txt', 'w')

'''
Python 파일 읽기
(1) readline() 
    - 파일의 한 줄을 가져와 문자열로 반환합니다. 파일 포인터는 그 다음줄로 이동합니다.

(2) readlines() 
    - 파일 내용 전체를 가져와 리스트로 반환합니다. 각 줄은 문자열 형태로 리스트의 요소로 저장됩니다.

예를들어 5줄짜리 파일을 readlines() 로 읽게 되면 문자열 5개를 요소로 갖는 리스트가 반환됩니다.


(3) read() 
    - 파일 내용 전체를 가져와 문자열로 반환합니다.
    readlines()와 마찬가지로 파일 내용 전체를 읽고, 파일 내용 전체를 하나의 문자열로 반환합니다.

각각의 줄은 '\n' 문자로 구분됩니다.

'''

f = open('test.txt', 'r')
r = f.readline()
r = f.readlines()
r = f.read()

f.write('요소')
f.close()



'''
sys.stdin
알고리즘 문제를 풀 때, 파이썬의 input()은 실행시간이 느려서 자주 시간초과가 난다. 이럴때 sys모듈의 stdin을 사용하면 더 빠르게 input이 가능하다.. 

'''

import sys

# sys.stdin - 여러줄 입력 받을 때
# sys.stdin은 ^Z를 입력받으면 종료
# 개행문자까지 입력된다.
nums = []
for line in sys.stdin:
    nums.append(line.strip()) # .strip 을 써서 개행 문자를 제거해줘야 함.
print(nums)
"""
1
2
3
4
5
^Z
['1', '2', '3', '4', '5']
"""

# sys.stdin.readline() - 한 줄 입력
x, y = sys.stdin.readline().split()
print("x = ", x)
print("y = ", y)
"""
x =  1
y =  2
"""

# sys.stdin.readline() 사용한 여러줄 입력
N = input()
a = [sys.stdin.readline() for _ in range(N)]
