'''
- Counter : 빈도출력 
    - 딕셔너리 형태로 key 값은 요소의 이름, value 값은 요소들의 횟수를 출력함.

    - 시간복잡도 O(N)
        - 리스트 내 원소 갯수 경우 for문 count를 n 번하면 O(N2)
        - count 여러 번 하는 경우 Counter 클래스가 더욱 유용
'''

from collections import Counter
b = 'sdfsdfsddddssAAADD'
c = 'sdfssswwqqazzA'

# Counter({'d': 6, 's': 5, 'A': 3, 'f': 2, 'D': 2})
print(Counter(b)) 
# Counter({'s': 4, 'w': 2, 'q': 2, 'z': 2, 'd': 1, 'f': 1, 'a': 1, 'A': 1})
print(Counter(c))

# 1. counter() 를 이용해 연산도 가능
# Counter({'s': 9, 'd': 7, 'A': 4, 'f': 3, 'D': 2, 'w': 2, 'q': 2, 'z': 2, 'a': 1})
print(Counter(b) + Counter(c))

print(Counter(c) - Counter(c))

# 2. 키로 값 조회, 변경 가능
counter = Counter("hello world")

print(counter["o"], counter["l"])

counter["l"] += 1
counter["h"] -= 1

# 3. most_common()
# 가장 빈도수가 높은 순으로 표시해주는 하수
# 같은 빈도수일 경우, 넣은 순으로 정렬됨.
# 인자값 : 그 숫자 번째까지의 빈도수를 표시해줌.
print(Counter('hello world').most_common(3))
