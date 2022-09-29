import sys
sys.stdin = open('sample_input.txt','r')
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(si,sj):
    que = deque()
    que.append((si,sj))
    distance[si][sj] = 0
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i+ di[k]
            nj = j + dj[k]
            if ni <0 or ni >= N or nj < 0 or nj >= N:
                continue
            diff =0
            if arr[ni][nj] > arr[i][j]:
                diff = arr[ni][nj] - arr[i][j]
            if distance[ni][nj] > distance[i][j] + 1 + diff:
                distance[ni][nj] = distance[i][j] + 1 + diff
                que.append((ni,nj))


for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]

    bfs(0,0)

    print("#{} {}".format(tc, distance[N-1][N-1]))