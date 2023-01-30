import sys
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().strip()
c = 0

for i in lst:
    x = s.count(i) 
    while x>0:
        y = s.find(i)
        c+=1
        x-=1  
        s = list(s)
        s[y:y+len(i)] = '-'
        s = ''.join(s) 
c+=len(s.replace('-', ''))
print(c)

#2
word = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    word = word.replace(i,'*')
print(len(word))