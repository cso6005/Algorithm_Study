import sys
lst = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

v = sys.stdin.readline()
c = ord(v[0]) - ord('a') + 1
i = int(v[1])
r = 0
for x in lst:
    I = i + x[0]
    C = c + x[1]

    if I <1 or C<1 or I >8 or C>8:
        continue
    r +=1
print(r)
