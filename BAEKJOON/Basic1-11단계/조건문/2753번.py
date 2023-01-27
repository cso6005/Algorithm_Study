x = int(input())
print('01'[(x%4==0) and (((x%100!=0) or (x%400==0)))])