import sys
t = 3
s = 0
i = 65
S = sys.stdin.readline().strip()            
while i < 91:
    if i in (80, 87):
        for j in range(i, i+4):
            s += S.count(chr(j)) * t
        i += 4
    else:
        for j in range(i, i+3):
            s += S.count(chr(j)) * t
        i += 3
    t += 1
print(s)

# 2
a=0
l='33344455566677788889990000'
for i in input():
    i=int(l[ord(i)-ord('A')])
    if i:a+=i
    else:a+=10
print(a)

#3
a=input()
c=len(a)
for i in a:
 c+=(ord(i)-ord('A')+6)//3
 if i in 'SVYZ':c-=1
print(c)