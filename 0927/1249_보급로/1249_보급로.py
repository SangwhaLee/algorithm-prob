import sys
sys.stdin = open('input.txt','r')

di = [-1,1,0,0]
dj = [0,0,-1,1]


def bfs(si, sj, total):


for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    minimum = 1e9
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True

    dfs(0,0,0)

    print(minimum)