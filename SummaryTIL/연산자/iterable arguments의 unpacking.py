''' 
Asterisk(*) 를 이용한 iterable arguments의 unpacking

    함수의 argument로 iterable한 값이 입력되었을 때 *를 사용해서 unpacking 할 수 있다.

    함수의 호출 시에 예제처럼 하나의 변수만 주는 것이 아니라 *나 **를 여러번 사용하여 
    값을 인자로 줄 수 있다. 이때 **의 경우에는 각 key arguments 중에 중복되는 key를 가진 데이터가 없는지 잘 확인해야한다. 
    파이썬에서는 같은 key의 argument가 여러번 정의될 수 없기 때문에 오류를 발생시키게 된다.

    (1) 리스트, 튜플 ... => iterable argument를 unpack => *['lemon', 'pear']
    (2) 딕셔너리 => keywork arguments를 unpack => **{'year': "2021", 'month': "04"}
'''

#(1)
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits[0], fruits[1], fruits[2], fruits[3] )# lemon pear watermelon tomato
print(*fruits) # lemon pear watermelon tomato # 각 원소가 콤마로 넣어지는 거와 같은 결과 !!

print(*fruits, sep='\n')

#(2)
date_info = {'year': "2021", 'month': "04", 'day': "14"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)
# '2021-04-14.txt'

''' 중요 !!
이를 활용하면 코드를 훨씬!! 줄일 수 있다.
리스트 내 각 원소를 연산 등 함수 적용하고 싶을 때
'''

print( *[ int(i) * -1 for i in '123'][::-1 ] ) # -3 -2 -1

