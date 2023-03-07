while True:
    try:
        n = int(input())
        paper = [0] * 300
        paper[0] = 1
        paper[1] = 1
        paper[2] = 3
        for i in range(3,n+1):
            paper[i] = paper[i-1]+2*paper[i-2]

        print(paper[n])
    except:
        break

