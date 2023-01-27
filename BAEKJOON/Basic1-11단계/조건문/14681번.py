x, y = int(input()), int(input())
print(1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4) 

print("3421"[x>0::2][y>0])