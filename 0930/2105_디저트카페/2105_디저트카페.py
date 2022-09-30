import sys
sys.stdin = open('sample_input.txt','r')

di = [1,1,-1,-1]
dj = [1,-1,-1,1]


def dessert_cafe(si,sj,direction, total):
    global max_types, startpoint
    # 시작점으로 돌아오면 그만

    if direction != 3:
        now_direction = [direction, direction + 1]
    else:
        now_direction = [direction]

    for d in now_direction:
        ni = si + di[d]
        nj = sj + dj[d]

        if startpoint[0] == ni and startpoint[1] == nj:
            max_types = max(total, max_types)
            return

        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if board[ni][nj] not in types:
            types.append(board[ni][nj])
            dessert_cafe(ni,nj,d,total+1)
            types.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_types = -1
    for i in range(N):
        for j in range(N):
            types = [board[i][j]]
            startpoint = [i,j]
            dessert_cafe(i,j,0,1)

    print("#{} {}".format(tc,max_types))