import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    first = ''
    second = ''
    third = ''
    fourth = ''
    fifth = ''
    if len(word) == 1:
        first = '..#..'
        second = '.#.#.'
        third = '#.' + word + '.#'
        fourth = '.#.#.'
        fifth = '..#..'
    elif len(word)>1:
        first = '..'
        for i in range(len(word)*2):
            if i == (len(word)*2-1):
                second += '.'
            else:
                second += '.#'
        for i in range(len(word)):

        third = '#.'+ '.#.'    + '.#'
