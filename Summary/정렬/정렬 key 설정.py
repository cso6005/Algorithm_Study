'''
1. sorted(word, key=word.find)
파이썬의 내장 함수인 sorted() 함수는 key라는 인수로 함수를 전달받아, 
해당 함수를 실행한 결과값을 기준으로 정렬을 진행하게 됩니다.
 => key를 word.find로 했을 때 순서대로 확인하면서 등장하는 단어와 동일한 단어로 정렬해준다.
 => 알파벳 순서와 상관없이 첫 등장한 위치부터 중복되는 단어를 순서대로 나열해주는 것이 특징이다
'''

word = 'abcdeaa'
print(sorted(word, key=word.find))
# >> ['a', 'a', 'a', 'b', 'c', 'd', 'e']

word = 'hello'
word2 = 'steve'
word = sorted(word, key=word.find)
word2 = sorted(word2, key=word2.find)
print(word, word2, sep='\n')
# >> ['h', 'e', 'l', 'l', 'o']
# >> ['s', 't', 'e', 'e', 'v']

''' 
2. sorted(words, key=lambda x : x.lower())
리스트에 str.lower()함수를 적용하여 정렬
'''
words = ['a', 'Albert' ,'Chris', 'Brown']
print(sorted(words, key=lambda x : x.lower()))
# >> ['a', 'Albert', 'Brown', 'Chris']

# 3
# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 4. 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]