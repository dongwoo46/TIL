n = int(input())
paper = [0] * 10000
paper[0] = 1
paper[1] = 1
paper[2] = 2
for i in range(3,n+1):
    paper[i] = paper[i-1]+paper[i-2]

print(paper[n]%10007)
