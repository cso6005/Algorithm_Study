from sys import stdin
N = int(stdin.readline().strip())
A = list(map(int, stdin.readline().split()))

vt = [A[0]]

def func(vt, i):
    start = 0
    end = len(vt)-1
    val = 0
    while start <= end:
        mid = (start + end)//2
        if vt[mid] < i:
            start = mid+1
        else:
            end = mid-1
            val = mid
    return val

for i in A[1:]:
    if vt[-1] < i:
        vt.append(i)
    else:
        val = func(vt, i)
        vt[val] = i

print(vt)
        
