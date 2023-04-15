s = input()
word = ''
tag = ''
tag_state = 0
idx = 0
if '<' in s:
    while True:
        if idx == len(s):
            print(word[::-1])
            break
        
        if tag_state:
            tag += s[idx]
            if s[idx] == '>':
                print(tag, end='')
                tag = ''
                tag_state = 0
            
        else:
            if s[idx] == '<': 
                tag_state = 1
                tag += '<'
                print(word[::-1], end='')
                word=''
            else:
                if s[idx] == ' ':
                    print(word[::-1], end=' ')
                    word=''
                else:
                    word += s[idx]
        idx +=1

else:
    ans = s.split(' ')
    for j in ans:
        print(j[::-1], end=' ')

# 다른 풀이
text = input().replace('<', 'X<').replace('>', '>X')
tag_str = [t for t in text.split('X') if t]

results = []
for ts in tag_str:
  if '<' in ts and '>' in ts:
    results.append(ts)
  else:
    words = ts.split()
    reversed_words = [word[::-1] for word in words]
    results.append(' '.join(reversed_words))

print(''.join(results))