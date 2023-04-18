def solution(new_id):
    alpha = [chr(i) for i in range(97, 123)]
    spec = ['.', '-', '_']
    numb = [str(i) for i in range(10)]
    temp = ''
    new_id = new_id.lower()
    if new_id:
        for x in new_id.lower():
            if x in alpha:
                temp += x
            elif x in spec:
                if temp:
                    if temp[-1] == '.' and x == '.':
                        continue
                temp += x
            elif x in numb:
                temp += x

    if temp:
        if temp[0] == '.':
            temp = temp[1:]
    if temp:
        if temp[-1] == '.':
            temp = temp[:-1]
    if len(temp) == 0:
        temp += 'a'

    if len(temp) >= 16:
        temp = temp[0:15]
        if temp[-1] == '.':
            temp = temp[:-1]
    if len(temp) <= 2:
        while len(temp) != 3:
            temp += temp[-1]

    answer = temp
    return answer