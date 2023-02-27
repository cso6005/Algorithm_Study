class Stack(list):

    push = list.append

    def peek(self):
        return self[-1]

s = Stack()

# 삽입
s.push(1)
s.push(2)

# 추출 - 반환 하고 없어짐
print(s.pop())

# 조회
print(s.peek())


# 2
s = []

# push
s.append(1)

# pop - 가장 마지막 원소를 추출하는 함수
print(s.pop()) 

# peek
print(s[-1])


# 큐 
q = []

q.append(1)

#  pop(0)의 time complexity는 O(N)이기 때문에 시간이 오래 걸린다.
# 따라서 시간 복잡도를 고려해 리스트는 큐로 사용하지 않는다.

q.pop(0)

q[0]

# 라이브러리

from queue import Queue 

q = Queue()

q.put(1)
q.put(2)

# 제일 앞에 것이 나온다.
q.get()


