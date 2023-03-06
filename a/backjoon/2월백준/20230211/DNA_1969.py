import sys
sys.stdin = open('../20230212/input', 'r')

n, m = list(map(int,input().split()))

dna_list = []
for i in range(n):
    dna_list.append(input())

dna =[[dna_list[j][i] for j in range(n)] for i in range(m)]
ans_dna = []
cnt = 0

for i in range(m):
    dna_spec = [0] * 4
    for j in range(n):
        if dna[i][j] == 'A':
            dna_spec[0] +=1
        elif dna[i][j] == 'C':
            dna_spec[1] += 1
        elif dna[i][j] == 'G':
            dna_spec[2] += 1
        else:
            dna_spec[3] += 1

    if dna_spec.index(max(dna_spec)) == 0:
        ans_dna.append('A')
    elif dna_spec.index(max(dna_spec)) == 1:
        ans_dna.append('C')
    elif dna_spec.index(max(dna_spec)) == 2:
        ans_dna.append('G')
    elif dna_spec.index(max(dna_spec)) == 3:
        ans_dna.append('T')

    cnt += n - dna_spec[dna_spec.index(max(dna_spec))]
    res = ''.join(ans_dna)
print(res)
print(cnt)



