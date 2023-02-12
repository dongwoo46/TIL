

def java_to_c(name):
    tmp = name[0]
    #이름의 맨 앞 글자가 대문자이면 에러
    if name[0].isupper():
        return 'Error!'
    # 새로 단어를 만든다고 생각해라 기존의 맨 앞글자에서 반복해서 체크하면서 각 알파벳을 붙임
    for i in range(1,len(name)):
        #만약 name[i]가 대문자면 name[0]에 '_'을 붙이고 name[i]를 소문자해서 붙임 아니면 그냥 붙임
        if name[i].isupper():
            tmp += '_'
            tmp += name[i].lower()
        else:
            tmp += name[i]
    return tmp

def c_to_java(name):
    # _가 두개 연속이면 에러
    for i in range(1, len(list(name))):
        if name[i - 1] == name[i] == '_':
            return 'Error!'
    # _가 이름의 양 끝에 있으면 에러
    if name[0] == '_' or name[-1] == '_':
        return 'Error!'
    # _를 기준으로 이름을 나눔

    name_list = name.split('_')

    #name_list가 문자나 숫자가 아니면 에러  만약 소문자로 바꿨을 때 기존과 다르면 에러
    for i in name_list:
        if not i.isalnum():
            return 'Error!'
        if i.lower() != i:
            return "Error!"
    # 단어의 시작 알파벳을 소문자로 바꿨을 때 기존과 다르면 에러
    for i in range(len(name_list)):
        if name_list[i][0].lower() != name_list[i][0]:
            return 'Error!'
    #name_list의 2번째부터 맨 앞 글자를 대문자로 바꿔줌
    for i in range(1, len(name_list)):
        name_list[i] = name_list[i].capitalize()
    #공백을 제거하고 합쳐서 리턴
    return ''.join(name_list)

answer_list = []
java_result_list = []

name = input()
alpha_big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
if '_' in name:
    if len(answer_list) == 0:
        answer_list.append(c_to_java(name))
else:
    if name.lower() == name:
        print(name)
    else:
        for i in alpha_big:
            if i in name:
                if len(answer_list) == 0:
                    answer_list.append(java_to_c(name))

if len(answer_list) > 0:
    print(''.join(answer_list))


