from collections import deque


def rotate_melting(ice, N, L):
    new_ice = [[0]*(2**N) for _ in range(2**N)]

    size = 2**L
    for y in range(0, 2 ** N, size):
        for x in range(0, 2 ** N, size):
            for i in range(size):
                for j in range(size):
                    new_ice[y+j][x+size-i-1] = ice[y+i][x+j]

    ice = new_ice
    temp = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N:
                    continue
                if ice[ni][nj] != 0:
                    cnt += 1
            if cnt < 3 and ice[i][j] !=0:
                temp.append((i,j))

    for i, j in temp:
        ice[i][j] -= 1

    return ice


def bfs(si, sj, N):
    global visited
    que = deque()
    visited[si][sj] = 1
    que.append((si,sj))
    size = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N:
                continue
            if ice[ni][nj] != 0 and visited[ni][nj] ==0:
                size += 1
                visited[ni][nj] = visited[i][j] + 1
                que.append((ni, nj))

    return size

N, Q = map(int,input().split())

ice = list(list(map(int,input().split())) for _ in range(2**N))

L = list(map(int,input().split()))

di = [-1,1,0,0]
dj = [0,0,-1,1]
total = 0
big_ice =0

for l in L:
    ice = rotate_melting(ice, N, l)

visited = [[0]*(2**N) for _ in range(2**N)]

for i in range(2**N):
    for j in range(2**N):
        total += ice[i][j]
        if ice[i][j] != 0 and visited[i][j] == 0:
            big_ice = max(bfs(i,j,N), big_ice)


# print(ice)
# print(visited)
print(total, big_ice)