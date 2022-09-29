import sys
sys.stdin = open('sample_input(1).txt','r')

di = [-1,1,0,0,-1,-1,1,1]
dj = [0,0,-1,1,-1,1,-1,1]


def setting(si, sj, type):
    if type == 1:
        board[si][sj] = 'b'
    else:
        board[si][sj] = 'w'
    for k in range(8):
        ni = si + di[k]
        nj = sj + dj[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue

        if type == 1 and board[ni][nj] == 'w':
            route = []
            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'w':
                    route.append((ni,nj))
                    ni += di[k]
                    nj += dj[k]
                elif board[ni][nj] == 'b':
                    for r in route:
                        board[r[0]][r[1]] = 'b'
                    break
                else:
                    break
        elif type == 2 and board[ni][nj] == 'b':
            route = []
            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'b':
                    route.append((ni, nj))
                    ni += di[k]
                    nj += dj[k]
                elif board[ni][nj] == 'w':
                    for r in route:
                        board[r[0]][r[1]] = 'w'
                    break
                else:
                    break


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 'w'
    board[N // 2][N // 2] = 'w'
    board[N // 2 -1][N // 2] = 'b'
    board[N // 2][N // 2 - 1] = 'b'

    for _ in range(M):
        x, y, t = map(int, input().split())
        si = y - 1
        sj = x - 1
        setting(si, sj, t)

    w_cnt = 0
    b_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'w':
                w_cnt += 1
            elif board[i][j] == 'b':
                b_cnt += 1

    print("#{} {} {}".format(tc, b_cnt, w_cnt))


