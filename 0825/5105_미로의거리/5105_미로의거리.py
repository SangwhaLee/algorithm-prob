import sys

sys.stdin = open('sample_input.txt', 'r')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(maze, i, j, N):
    visited = [[0]*N for _ in range(N)]
    que = list()
    visited[i][j] = 0
    que.append((i, j))
    while que:
        t = que.pop(0)
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == '3':
                return visited[t[0]][t[1]]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == '0':
                maze[ni][nj] = '1'
                visited[ni][nj] = visited[t[0]][t[1]] + 1
                # print("i: {}, j: {}, range:{}".format(ni, nj, visited[ni][nj]))
                que.append((ni,nj))

    return 0


for tc in range(1,int(input())+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    for i in range(N):
        for j  in range(N):
            if maze[i][j] == '2':
                si = i
                sj = j

    ans = bfs(maze, si, sj, N)
    print("#{} {}".format(tc, ans))
