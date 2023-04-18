from sys import stdin

array1 = []
array2 = []
[array1.append(list(map(int, stdin.readline().split()))) for _ in range(5)]
[ array2.extend(list(map(int, stdin.readline().split()))) for _ in range(5)]

def check():
    diag1 = 0
    diag2 = 0
    cnt = 0
    for i in range(5):
        col = 0
        for j in range(5):
            col += array1[j][i]
        if col == 0:
            cnt+=1
        if array1[i][i] == 0:
            diag1 +=1
            
        if diag1 == 5:
            cnt +=1

        if array1[i][4-i] == 0:
            diag2 +=1
        if diag2 == 5:
            cnt += 1
            
        if sum(array1[i]) == 0:
            cnt+=1    

    if cnt >= 3:
        return True
    return False


def func():
    answer = 0
    for n in array2:
        answer += 1
        for i in range(5):
            for j in range(5):
                if array1[i][j] == n:
                    array1[i][j] = 0

        if check():
            print(answer)
            break
                
                        
func()
                    
 