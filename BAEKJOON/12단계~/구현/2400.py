from sys import stdin
val = "ABCDE"
for _ in range(3): 
    zero  = stdin.readline().count('0')
    print(val[zero-1])
    
    # if zero == 1:
    #     print("A")
    # elif zero == 2:
    #     print("B")
    # elif zero == 3:
    #     print("C")
    # elif zero == 4:
    #     print("D")        
    # else:
    #     print("E")