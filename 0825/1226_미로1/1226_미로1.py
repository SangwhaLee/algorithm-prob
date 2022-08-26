import sys
sys.stdin = open('input.txt','r')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(maze, i, j, N):
    visited = [[0]*(N) for _ in range(N)]
    que = []
    que.append((i,j))
    visited[i][j] = 0

    while que:
        t = que.pop(0)
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 < ni <= N and 0 < nj <= N and maze[ni][nj] == '3':
                return 1
            if 0 < ni <= N and 0 < nj <= N and maze[ni][nj] == '0':
                maze[ni][nj] = '1'
                visited[ni][nj] = visited[t[0]][t[1]] + 1
                que.append((ni, nj))

    return 0


for tc in range(1, 11):
    N = int(input())
    maze = [list(input()) for _ in range(16)]

    print("#{} {}".format(tc, bfs(maze, 1, 1, 16)))