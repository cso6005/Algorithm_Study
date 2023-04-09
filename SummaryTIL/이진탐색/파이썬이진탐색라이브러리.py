'''
이진 탐색 라이브러리
=> 배열은 오름차순 정렬이 되어있음을 보장해야 한다.
'''
# 1. bisect_left(a, x) 
#   정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# 2. bisect_right(a, x) 
#   정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# ex 활용)
# 값이 특정 범위에 속하는 데이터 개수 구하기 (
# 값의 범위가 매우 클 때 선형탐색의 경우 시간초과이다. ex. count()
# 이러한 경우, 이진탐색 알고리즘을 사용해야 하고, 파이썬은 이와 같은 라이브러리를 제공한다.
def func(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(func(a, 4, 4))
print(func(a, -1, 3))