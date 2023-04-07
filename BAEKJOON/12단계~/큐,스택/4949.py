from sys import stdin

while True:
    s = stdin.readline().rstrip()
    if s == '.':
        break
    string = ''

    for i in s:
        if i in '()[]':
            string += i
    
    while string:
        if '()' in string:
            string = string.replace('()', '')
        elif '[]' in string:
            string = string.replace('[]', '')
        else:
            print('no')
            break

    if not string:
        print("yes")

    