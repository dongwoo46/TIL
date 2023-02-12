import sys
sys.stdin = open('../20230212/input', 'r')
n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

row = paper
col = [[paper[j][i] for j in range(n)] for i in range(2)]
row_10 = []
col_10 = []
print(row)
print(col)

for i in range(n):
    row_10.append(col[0][i]+10)
    col_10.append(col[1][i]+10)

row_length = max(row_10)+min(col[0])
col_length = max(col_10)+ min(col[1])


all_row =  col[0]+row_10
all_col =  col[1]+col_10
all_row = list(all_row)
all_col = list(all_col)
all_row.sort()
all_col.sort()

print(all_row)
print(all_col)
