import sys
sys.stdin = open('input','r')
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))[1:]
    b = list(map(int,input().split()))[1:]
    a_cnt4 = a.count(4)
    b_cnt4 = b.count(4)
    a_cnt3 = a.count(3)
    b_cnt3 = b.count(3)
    a_cnt2 = a.count(2)
    b_cnt2 = b.count(2)
    a_cnt1 = a.count(1)
    b_cnt1 = b.count(1)
    if a_cnt4>b_cnt4:
        print('A')
    elif b_cnt4> a_cnt4:
        print('B')
    else:
        if a_cnt3 > b_cnt3:
            print('A')
        elif b_cnt3>a_cnt3:
            print('B')
        else:
            if a_cnt2 > b_cnt2:
                print('A')
            elif b_cnt2 > a_cnt2:
                print('B')
            else:
                if a_cnt1 > b_cnt1:
                    print('A')
                elif b_cnt1 > a_cnt1:
                    print('B')
                else:
                    print('D')