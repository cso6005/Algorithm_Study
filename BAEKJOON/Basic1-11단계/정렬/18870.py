# 좌표 압축 알고리즘을 활용한 ranking list

from sys import stdin
stdin.readline()
lst = list(map(int, stdin.readline().split()))
lst_s = sorted(set(lst))

dic = { val:idx for idx, val in enumerate(lst_s)}
[print(dic[i] , end=' ') for i in lst]


'''
처음에는 리스트에서 index함수로 출력 할 값을 찾았다.
그러나, 이는 시간초과
list.index(i)의 형태는 시간복잡도 O(N)을 가지고 있고 
그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 돼서
시간초과가 나는 것이었다.
    => 그렇기에 dict 사용 복잡도 O[1]
        {val:idx} 로 키에 해당 값, 값에 해당 값의 인덱스를 넣어주었다.

list.index(i) 형태의 시간 복잡도 = O(N)
index[i] 형태의 시간 복잡도 = O(1)
'''