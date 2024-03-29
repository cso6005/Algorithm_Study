'''
알고리즘을 하다보면, 소수점 뿐만아니라 정수 또한
자리수를 맞춰줘야 할 때가 있다.
문자열 포맷은 여러 방법이 있지만, 난 format() 함수로 진행하고자 한다.
    1. 소수점을 일정 자리수까지 자르기
    2. 정수 앞에 0 을 붙여 자리수를 맞추기
        => 문자열 formatting
            {인덱스:조건}.format(대상)
'''
a=123
b=3.1415

print('a:{0:4d}'.format(a)) # 공백으로 채워짐 # a: 123
print('a:{0:04d}'.format(a)) # 0으로 채워짐 # a:0123

print('{0:04d}{1:.2f}'.format(a, b)) # 01233.14

# b가 0000003.14가 아닌 이유 ?
# 소수점이하와 소수점을 모두 포함해서 개수를 샌다. 
# 소수점 1개 + 소수점 이하 2개 + 정수부분 4개 = 총 7 개
print('b:{0:07.2f}'.format(b)) # b:0003.14
print('b:{1:07.2f}'.format(a,b)) # b:0003.14
