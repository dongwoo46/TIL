import sys
sys.stdin = open('input', 'r')
n,m,l = map(int,input().split())
board = [[list(map(int,input().split())) for _ in range(m)] for _ in range(l)]
print(board[1][1][3])