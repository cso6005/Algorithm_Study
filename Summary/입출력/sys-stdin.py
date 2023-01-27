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
