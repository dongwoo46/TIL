import sys
sys.stdin = open('input','r')

def selectionsort(arr):
    for i in range(len(arr)):
        minidx = i
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                minidx = j
        arr[i], arr[j] = arr[j], arr[i]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    # max_numb = numbers[-1:-6:-1]
    # min_numb = numbers[0:5]
    ans_list = [0] * 10

    for i in range(10):
        if i%2==0:
            ans_list[i]= numbers.pop()
        else:
            ans_list[i] = numbers.pop(0)

    print(f'#{tc}', *ans_list)



