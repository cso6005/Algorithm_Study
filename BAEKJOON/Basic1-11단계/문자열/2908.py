import sys
A, B = sys.stdin.readline().split()
print(A[::-1]) if A[::-1] > B[::-1] else print(B[::-1])

# int() 정수로 타입 변경 하지 않아도 string 상태여도 비교 가능 ! 

#2 max() 이용 !!
print(max(input()[::-1].split()))