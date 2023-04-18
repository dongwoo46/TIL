dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
       'eight': '8', 'nine': '9'}


def solution(s):
    string = ''
    answer = ''
    for i in s:
        if i.isdigit(): # i가 숫자이면 answer에 그냥 붙이고
            answer += str(i)
        else:
            string += i # 숫자가 아니면 string은  i 가된다
            if string in dic: # 해당 숫자가  dic안에 있다면
                answer += dic[string] # answer에 해당 key의 value를 더해줌
                string = '' # string초기화

    return int(answer)