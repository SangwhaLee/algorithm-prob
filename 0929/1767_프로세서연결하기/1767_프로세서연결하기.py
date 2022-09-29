import sys
sys.stdin = open('sample_input.txt','r')

di = [-1,1,0,0]
dj = [0,0,-1,1]


def dfs(depth, total):
    global minimum
    if depth == len(cpus):
        minimum = min(total, minimum)
        return

    if total >= minimum:
        return

    for k in range(4):
        line = []
        ni = cpus[depth][0] + di[k]
        nj = cpus[depth][1] + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if board[ni][nj] == 0 and visited[ni][nj] == 0:
            thisline = True
            while not (ni < 0 or ni >= N or nj < 0 or nj >= N):
                line.append((ni, nj))
                ni += di[k]
                nj += dj[k]
                if visited[ni][nj] == 1 or board[ni][nj] == 1:
                    thisline = False
                    break
                if thisline:
                    cnt = 1
                    for r in line:
                        visited[r[0]][r[1]] = 1
                        cnt += 1
                    dfs(depth+1, total + cnt)
                    for r in line:
                        visited[r[0]][r[1]] = 0


for tc in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    cpus = []
    visited = [[0]*N for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] != 0:
                cpus.append((i,j))

    minimum = float('inf')
    dfs(0, 0)
    print(minimum)
