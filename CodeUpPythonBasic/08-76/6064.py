# 삼항 연산 if문

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

#16ms
print( x if x < y and x < z else y if y < z and y < x else z)

#14ms
print( (x if x<y else y) if ((x if x<y else y) < z) else z)