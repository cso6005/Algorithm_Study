from sys import stdin

mo = 'aeiou'
while True:
    word = stdin.readline().strip()
    if word == 'end':
        break
    n = len(word)
    rule = True
    rule1 = False
    for ch in word:
        if ch in mo:
            rule1 = True

    if not rule1:
        rule = False

    for idx in range(0,n-1):
        if word[idx] == word[idx+1]:
            if word[idx] == 'e' or word[idx] == 'o':
                continue
            rule = False
 
    for idx in range(0,n-2):
        mo_cnt = 0
        if word[idx] in mo:
            mo_cnt += 1
        if word[idx+1] in mo:
            mo_cnt += 1
        if word[idx+2] in mo:
            mo_cnt += 1

        if mo_cnt == 3 or mo_cnt ==0:
            rule = False
            break
    
    if rule:
        print("<"+word+"> is acceptable.")
    else:
        print("<"+word+"> is not acceptable.")

