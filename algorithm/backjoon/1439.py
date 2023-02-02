s = input()

cnt1 = 0 #1을 뒤집음
cnt0 = 0 #0을 뒤집음


if s[0] == '1':
    cnt1 +=1
else:
    cnt0+=1



#모두 0으로 만듦
for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] == '1':
                cnt1+=1
# 모두 1로 만듦
for i in range(len(s)-1):
       if s[i] != s[i+1]:
            if s[i+1] == '0':
                cnt0 += 1

if cnt1<cnt0:
    print(cnt1)
else:
    print(cnt0)


