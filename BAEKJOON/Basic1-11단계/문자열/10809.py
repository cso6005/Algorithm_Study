import sys
S = sys.stdin.readline().strip()

[print(S.find(c), end=' ') for c in [chr(i) for i in range(97, 123)]]

[print(S.find(chr(i))) for i in range(97, 123)]