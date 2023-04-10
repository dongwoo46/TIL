discount = [10, 20, 30, 40]

def solution(users, emoticons):
    # answer = [(이모티콘 가입자수, 이모티콘 매출액)]
    # users = [(할인율,  이모티콘 가입한도)]
    # emoticons = [(각 이모티콘 가격)]
    answer = [0,0]
    dis_list = []
    def backtrack(v):
        nonlocal answer
        if v == len(emoticons):
            cnt = total = 0
            for i in range(len(users)):
                temp = 0
                for j in range(len(emoticons)):
                    if users[i][0] <=dis_list[j]:
                        temp += emoticons[j]*(100-dis_list[j])//100
                if temp>=users[i][1]:
                    cnt+=1
                else:
                    total += temp
            if cnt > answer[0] or (cnt==answer[0] and total>answer[1]):
                answer = [cnt, total]
            return


        for i in range(4):
            dis_list.append(discount[i])
            backtrack(v+1)
            dis_list.pop()
    backtrack(0)
    return answer