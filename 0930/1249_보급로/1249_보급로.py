import sys
sys.stdin = open("input.txt",'r')
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]


def bfs(si,sj):
    que = deque()
    visited[si][sj] = 0
    que.append((si,sj))
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if visited[ni][nj] == -float('inf'):
                visited[ni][nj] = visited[i][j]+board[ni][nj]
                que.append((ni, nj))
            elif visited[ni][nj] > visited[i][j]:
                visited[ni][nj] = min(visited[ni][nj], visited[i][j]+board[ni][nj])
                que.append((ni,nj))


for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int,list(input()))) for _ in range(N)]
    visited = [[-float('inf') for _ in range(N)] for _ in range(N)]
    bfs(0,0)
    print("#{} {}".format(tc,visited[N-1][N-1]))