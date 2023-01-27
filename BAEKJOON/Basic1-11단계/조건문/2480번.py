a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(sorted([a, b, c])[-1]*100)

# max(1,2,3, ..) 인자 여러 개 가능!
# print(10000+1000*a if a==b==c else 1000+100*b if a==b or b==c else 1000+100*a if c==a else 100*max(a, b, c))

            



