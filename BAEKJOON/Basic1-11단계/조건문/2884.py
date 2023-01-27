H, M = map(int, input().split())
print(H, M-45) if M >= 45 else  print(23, M+15) if H == 0 else print(H-1, M+15)

# 2
total = H*60+M-45
if total < 0:
    total+=60*24
print(total//60, total%60)