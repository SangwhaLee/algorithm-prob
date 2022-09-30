import sys
sys.stdin = open('sample_input.txt','r')

di = [-1,1,0,0]
dj = [0,0,-1,1]


def dfs(si,sj, canAfford, cnt):
    global max_length
    error_cnt = 0
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]:
            continue
        if mountain[ni][nj] < mountain[si][sj]:
            visited[ni][nj] = True
            dfs(ni, nj, canAfford, cnt +1)
            visited[ni][nj] = False
        else:
            if (mountain[ni][nj] - mountain[si][sj]) < K and canAfford:
                tmp = mountain[ni][nj]
                mountain[ni][nj] = mountain[si][sj] - 1
                visited[ni][nj] = True
                dfs(ni, nj, False, cnt+1)
                visited[ni][nj] = False
                mountain[ni][nj] = tmp

    max_length = max(max_length, cnt)


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    max_height = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_height:
                max_height = mountain[i][j]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                visited = [[False]*N for _ in range(N)]
                visited[i][j] = True
                dfs(i,j,True,1)

    print("#{} {}".format(tc, max_length))