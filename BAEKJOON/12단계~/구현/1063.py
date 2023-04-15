from sys import stdin
king, stone, n = stdin.readline().split()
move = []
[move.append(stdin.readline().strip()) for _ in range(int(n))]
king = [ord(king[0]), int(king[1])]
stone = [ord(stone[0]), int(stone[1])]

col, idx = king[0], king[1]
s_col, s_idx = stone[0], stone[1]
for m in move:
    if m == 'R':
        col = king[0] + 1
    elif m == 'L':
        col = king[0] - 1
    elif m == 'B':
        idx = king[1] - 1
    elif m == 'T':
        idx = king[1] + 1
    elif m == 'RT':
        col = king[0] + 1
        idx = king[1] + 1
    elif m == 'LT':
        col = king[0] - 1
        idx = king[1] + 1
    elif m == 'RB':
        col = king[0] + 1
        idx = king[1] - 1
    else:
        col = king[0] - 1
        idx = king[1] - 1
    if idx < 1 or col < ord('A') or idx > 8 or col > ord('H'):
        continue

    if col == stone[0] and idx == stone[1]:
        s_col = stone[0] +(col-king[0])
        s_idx = stone[1] + (idx-king[1])
        if s_idx < 1 or s_col < ord('A') or s_idx > 8 or s_col > ord('H'):
            continue

    stone[0], stone[1] = s_col, s_idx
    king[0], king[1] = col, idx

print(chr(king[0]), king[1], sep='')
print(chr(stone[0]), stone[1], sep='')