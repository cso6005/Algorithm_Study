# 별찍기

def draw_stars(n):

    if n==1:
        return ['*']

    Stars=draw_stars(n//3) # Stars는 리턴값 L(이전 재귀함수의) 이된다.
    L=[]
    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)
    print(L)
    return L

N=int(input())
print('\n'.join(draw_stars(N)))