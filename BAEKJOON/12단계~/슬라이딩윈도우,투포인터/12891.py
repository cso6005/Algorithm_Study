from sys import stdin
s, p = map(int, stdin.readline().split())
dna = stdin.readline().strip()
A,C,G,T = map(int, stdin.readline().split())
dic = {'A':0,'C':0,'G':0,'T':0} 
answer = 0

for ch in dna[:p-1]:
    dic[ch]+=1

for idx in range(p-1,s):
    dic[dna[idx]]+=1

    if dic['A']>=A and dic['C']>=C and dic['G']>=G and dic['T']>=T:
        answer+=1

    dic[dna[idx-p+1]]-=1

print(answer)
