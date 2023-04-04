import sys
sys.stdin = open('input', 'r')
import heapq
h = []
h_max = []

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    for i in range(n):
        ord, numb = map(int,input().split())
