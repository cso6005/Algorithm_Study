func = list(input().split('-'))

result = sum(map(int, func[0].split('+')))
if len(func) > 1:
    for i in func[1:]:
        result -= sum(map(int, i.split('+')))            
print(result) 

# 해당 문자열에 구분자가 없다면, 오류 나는 것이 아니라, 없는 대로
# split 안 되고 원본 문자열 그대로 리턴됨. => 플러스가 있는지 없는지 확인할 필요 없음.
func = list(input().split('-'))
if '+' in func[0]:
    result = sum(map(int, func[0].split('+')))
else:    
    result = int(func[0])
if len(func) > 1:
    for i in func[1:]:
        if '+' in i:
            result -= sum(map(int, i.split('+')))            
        else:
            result -= int(i)
print(result)  
 