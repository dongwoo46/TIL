import sys
sys.stdin = open("input", "r")

for tc in range(1,11):
    n = int(input())
    box = list(map(int,input().split()))


    for i in range(n):
        max_height = max(box)
        min_height = min(box)
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))
        box[max_idx] -=1
        box[min_idx] +=1
        max_min_sub = max(box) - min(box)
        if max_height - min_height == 0:
            break


    print(f'#{tc} {max_min_sub}')

'''
def get_max_idx():
    max_value = 0 #가지고 올 값보다 작은거 설정
    max_idx = -1 #인덱스는 0도 있기때문에 성립하지않는 -1로 설정
    for i i n range(len(boxes)):
        if boxes[i] > max_value:
            max_value = boxes[i]
            max_value = i
    return max_idx
     
def get_min_idx():
    min_value = 10000000000000000 #가지고올 값보다 아주큰값설정
    min_idx = -1
    for i in range(len(boxes)):
        if boxes[i]<min_value:
            min_value = boxes[i]
            min_idx = i
    return min_idx
    
for tc in range(1,11):
    n = int(input()
    boxes = list(map(int,input().split()))
    for i in range(n):
        boxes[get_max_idx()] -= 1
        boxes[get_min_idx()] += 1
                
    res = boxes[get_max_idx{}] - boxes[get_min_idx]
    print(f'#{tc} {res}'''







