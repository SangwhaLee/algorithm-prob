import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    # 90도 돌린 배열이 저장될 리스트
    ninety = [[] for _ in range(N)]
    # 270도 돌린 배열이 저장될 리스트
    twoSeven = [[] for _ in range(N)]
    # 180도 돌린 배열이 저장될 리스트
    oneEight = [[] for _ in range(N)]

    # 90 돌린 배열의 전개를 보면 y값이 먼저 N-1 ~ 0으로 순회를 돌고 그 다음에 x값이 0 ~ N-1로 순회한다
    i_step = 0
    for i in range(N):
        for j in range(N-1,-1,-1):
            ninety[i_step].append(str(arr[j][i]))
        i_step += 1

    # print(ninety)

    # 180도 돌린 배열의 전개는 x값이 먼저 N-1 ~ 0으로 순회를 돌고 그 다음에 y값이 N-1~0으로 순회를 돈다
    i_step = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            oneEight[i_step].append(str(arr[i][j]))
        i_step += 1

    # print(oneEight)

    # 270도 돌린 배열의 전개는 y값이 먼저 0~N-1로 순회를 돌고 그 다으메 x값이 N-1~0으로 순회를 돈다
    i_step = 0
    for i in range(N-1, -1, -1):
        for j in range(N):
            twoSeven[i_step].append(str(arr[j][i]))
        i_step += 1

     # print(twoSeven)

    ans = []

    # 각 리스트의 같은 위치에 있는 값을 하나의 문자열로 만들어 ans에 저장
    for i in range(N):
        ans.append(''.join(ninety[i]) + ' ' + ''.join(oneEight[i]) + ' ' + ''.join(twoSeven[i]))

    print("#{}".format(tc))
    for i in range(N):
        print(ans[i])

