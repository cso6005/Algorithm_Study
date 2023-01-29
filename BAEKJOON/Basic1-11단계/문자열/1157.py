import sys
S = sys.stdin.readline().strip().upper()

v = {i:S.count(i) for i in set(S)}
m = max(v.values())
s = ''

for idx, val in v.items():
    if val == m:
        s += idx
print(s) if len(s) == 1 else print('?')

# 2
str = input().upper()
max_num = 0
max_char = ''
for i in range(26):
    cnt = str.count(chr(i + 65))
    if max_num < cnt:
        max_num = cnt
        max_char = chr(i + 65)
    elif max_num == cnt:
        max_char = "?"
print(max_char)