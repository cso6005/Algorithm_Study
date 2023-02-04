from sys import stdin
lst_1 = [i for i in range(int(stdin.readline().strip())+1, 3, -1)]
# 0 ~ N-1

# 초기에 이번 두번 옮김.
lst_3 = [1] # 젤 위 꺼 먼저 빼주기
lst_2 = [2] 
print(lst_1)
print(lst_2)
print(lst_3)

def func(n):
    if len(lst_1) == 0:
        return n 
    
    else:
        if 1:
            print()

        if len(lst_3) == 0:
            lst_3.append(lst_1.pop(-1))

        elif len(lst_2) == 0:
            lst_2.append(lst_1.pop(-1))

        else:
            if lst_2[0] > lst_3[0]:
                lst_2.append(lst_3[-1])
            else:
                lst_3.append(lst_2[-1])

        if lst_3[0] > n :
            lst_3.append(lst_1.pop(n))
        elif lst_2[0] > n:
            lst_2.append(lst_1.pop(n))
        
        n+=1

func(3)

