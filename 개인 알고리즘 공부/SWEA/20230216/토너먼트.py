def f(i,j): # i~j번까지 승자 찾는 함수
    if i == j: #한명만 남은경우
        return 1
    else: # 두명 이상인 경우 두 그룹의 승자를 뽑아서 최종 승자 찾기
        left = f(i, (i+j)//2) # 왼쪽 그룹의 승자
        right = f((i+j)//2+1,j) #오른쪽 그룹의 승자
        return win(left,right) # 최종승자
