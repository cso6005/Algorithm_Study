N = input()
lst = list(map(int, input().split()))
v = int(input())
print(lst.count(v))

# 문자열로 구분하려고 하는 경우 만약 
# 음수인 경우에는 -3 이 아닌 -,3 으로 찾아진다.
# 이때문에 문자열이 아닌 리스트에 담아 진행해야 한다.

