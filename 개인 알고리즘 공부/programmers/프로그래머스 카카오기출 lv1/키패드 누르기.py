dic_left = {1: 'L', 4: 'L', 7: 'L'} #왼손으로 누르는 key 값들
dic_right = {3: 'R', 6: 'R', 9: 'R'} # 오른손으로 누르는 값들
dic_loc = {1: (0, 0), 4: (1, 0), 7: (2, 0), 3: (0, 2), 6: (1, 2), 9: (2, 2), '*': (3, 0), '#': (3, 2), 0: (3, 1),
           2: (0, 1), 5: (1, 1), 8: (2, 1)} # 해당 번호를 눌럿을 때 손의 위치


def solution(numbers, hand):
    answer = ''
    right = [3, 2]
    left = [3, 0]
    for i in numbers:
        if i in dic_left: # 왼손으로 누르는 값에 있으면
            answer += dic_left[i] # L 추가
            left[0], left[1] = dic_loc[i] # 왼손의 위치 조정
        elif i in dic_right:  # 오른손으로 누르는 값이면
            answer += dic_right[i] # R 추가
            right[0], right[1] = dic_loc[i] # 오른손 위치 조정
        else: # 가운데에 잇는 애들이라면
            if i == 2: # i = 2일 때
                dist_left = abs(left[0] - dic_loc[i][0]) + abs(left[1] - dic_loc[i][1]) # 왼손이 해당 번호까지의 거리
                dist_right = abs(right[0] - dic_loc[i][0]) + abs(right[1] - dic_loc[i][1]) # 오른손이 해당 번호까지의 거리
                if dist_left > dist_right: # 만약 왼손 거리가 더길면
                    right[0], right[1] = dic_loc[i] # 오른손으로 클릭 즉 오른손 위치 변화
                    answer += 'R' # R 추가
                elif dist_left < dist_right: # 오른손 거리가 더길면
                    left[0], left[1] = dic_loc[i] # 왼손거리 조정
                    answer += 'L' # L추가
                elif dist_left == dist_right: # 왼쪽 오른쪽 거리가 같으면
                    if hand == 'right': # 오른손 잡이면 오른손 추가 왼손잡이면 왼손 추가
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    elif hand == 'left':
                        left[0], left[1] = dic_loc[i]
                        answer += 'L'

            elif i == 5:
                dist_left = abs(left[0] - dic_loc[i][0]) + abs(left[1] - dic_loc[i][1])
                dist_right = abs(right[0] - dic_loc[i][0]) + abs(right[1] - dic_loc[i][1])
                if dist_left > dist_right:
                    right[0], right[1] = dic_loc[i]
                    answer += 'R'
                elif dist_left < dist_right:
                    left[0], left[1] = dic_loc[i]
                    answer += 'L'
                else:
                    if hand == 'right':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    elif hand == 'left':
                        left[0], left[1] = dic_loc[i]
                        answer += 'L'

            elif i == 8:
                dist_left = abs(left[0] - dic_loc[i][0]) + abs(left[1] - dic_loc[i][1])
                dist_right = abs(right[0] - dic_loc[i][0]) + abs(right[1] - dic_loc[i][1])
                if dist_left > dist_right:
                    right[0], right[1] = dic_loc[i]
                    answer += 'R'
                elif dist_left < dist_right:
                    left[0], left[1] = dic_loc[i]
                    answer += 'L'
                else:
                    if hand == 'right':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    elif hand == 'left':
                        left[0], left[1] = dic_loc[i]
                        answer += 'L'

            else:
                dist_left = abs(left[0] - dic_loc[i][0]) + abs(left[1] - dic_loc[i][1])
                dist_right = abs(right[0] - dic_loc[i][0]) + abs(right[1] - dic_loc[i][1])
                if dist_left > dist_right:
                    right[0], right[1] = dic_loc[i]
                    answer += 'R'
                elif dist_left < dist_right:
                    left[0], left[1] = dic_loc[i]
                    answer += 'L'
                else:
                    if hand == 'right':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    elif hand == 'left':
                        left[0], left[1] = dic_loc[i]
                        answer += 'L'

    return answer