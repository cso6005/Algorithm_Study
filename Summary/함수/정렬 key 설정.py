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


