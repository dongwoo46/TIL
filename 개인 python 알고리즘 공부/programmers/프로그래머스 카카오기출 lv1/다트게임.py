def solution(dartResult):
    answer= 0
    tmp = ''
    result = [0]*4
    cnt = 0 # 몇번째 위치까지 결정났는가
    for i in range(len(dartResult)):
        if dartResult[i].isdigit(): # 다트가 숫자이면
            tmp+=dartResult[i] # tmp에 값을 더해줌
        elif dartResult[i] == 'S': #S,D,T 나오면 다트한게임이 끝난 것
            result[cnt] = int(tmp) # 다트게임이 하나 끝났으니까
            tmp = '' # tmp초기화 하고
            cnt +=1 # cnt 개수 증가
        elif dartResult[i] == 'D': #D이면 해당 cnt위치의 값을 제곱해줌
            result[cnt] = int(tmp)**2
            tmp = ''
            cnt+=1
        elif dartResult[i] == 'T': # T이면 해당 cnt위치를 세제곱
            result[cnt] = int(tmp)**3
            tmp = ''
            cnt+=1
        elif dartResult[i] == '#': # #이면 해당 위치값을 음수로 바꿔줌
            result[cnt-1] = result[cnt-1]*(-1)
        elif dartResult[i] == '*': # '*'이면 cnt에 따라서  cnt-1부터 cnt가 0일 때까지 해당 위치의 값들을 다 2배해줌
            if cnt == 1:
                result[0] = result[0]*2
            elif cnt == 2:
                result[0] = result[0]*2
                result[1] = result[1]*2
            elif cnt == 3:
                result[1] = result[1]*2
                result[2] = result[2]*2
    answer = sum(result)
    return answer


