dic_left = {1: 'L', 4: 'L', 7: 'L'}
dic_right = {3: 'R', 6: 'R', 9: 'R'}
dic_loc = {1: (0, 0), 4: (1, 0), 7: (2, 0), 3: (0, 2), 6: (1, 2), 9: (2, 2), '*': (3, 0), '#': (3, 2), 0: (3, 1),
           2: (0, 1), 5: (1, 1), 8: (2, 1)}


def solution(numbers, hand):
    answer = ''
    dist_left = 0
    dist_right = 0
    right = [3, 2]
    left = [3, 0]
    for i in numbers:
        if i in dic_left:
            answer += dic_left[i]
            left[0], left[1] = dic_loc[i]
        elif i in dic_right:
            answer += dic_right[i]
            right[0], right[1] = dic_loc[i]
        else:
            if i == 2:
                dist_left = abs(left[0] - dic_loc[i][0]) + abs(left[1] - dic_loc[i][1])
                dist_right = abs(right[0] - dic_loc[i][0]) + abs(right[1] - dic_loc[i][1])
                if dist_left > dist_right:
                    right[0], right[1] = dic_loc[i]
                    answer += 'R'
                elif dist_left < dist_right:
                    left[0], left[1] = dic_loc[i]
                    answer += 'L'
                else:
                    if hand == 'R':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    else:
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
                    if hand == 'R':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    else:
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
                    if hand == 'R':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    else:
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
                    if hand == 'R':
                        right[0], right[1] = dic_loc[i]
                        answer += 'R'
                    else:
                        left[0], left[1] = dic_loc[i]
                        answer += 'L'

    return answer
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers,hand))