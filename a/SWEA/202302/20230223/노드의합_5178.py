import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n,m,l = map(int,input().split()) # n는 총 노드 수 /m은 리프노드 수/ l 필요한 값의 노드 번호
    tree = [0]*(n+1)

    # node, value에 맞게 tree에 값을 집어 넣음
    for _ in range(m):
        node,value = map(int,input().split())
        tree[node] = value

    #만약 n이 홀수로 끝나면 마지막에 혼자 남는게 아니라 둘이 짝 지어질때
    if n%2==1:
        #last =n / pre_last = n-1 로 설정
        last = n
        pre_last = n - 1
        #tree[1]가 0이 아닐때까지 즉 루트에 값이 입력될때까지 실행
        while tree[1] == 0:
            #p부모 노드는 last를 2로 나눈 몫
            p = last // 2
            #따라서 해당 p의 값은 tree의 last값과 pre_last값을 합하여 결정
            tree[p] = tree[last] + tree[pre_last]
            #2노드씩 줄여가면서 노드를 합해 부모 노드 값 구함
            last -=2
            pre_last -=2
    # 만약 n이 짝수로 끝나면 마지막 하나가 혼자 달랑 남아있음
    else:
        #마지막 n을 most_last로둔다
        most_last = n
        last = n-1
        pre_last = n-2
        # most_last의 부모 노드는 most_last혼자 이기 때문에 most_last의 값 그대로 올라감
        tree[most_last//2] = tree[most_last]
        #계속해서 tree[1]에 값이 들어올때까지 반복
        while tree[1] == 0:
            #n이 홀수 일때랑 동일
            p = last // 2
            tree[p] = tree[last] + tree[pre_last]
            last -= 2
            pre_last -= 2

    print(f'#{tc}', tree[l])
