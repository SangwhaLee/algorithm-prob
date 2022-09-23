import sys
sys.stdin = open('sample_input.txt','r')

di = [-1,1,0,0]
dj = [0,0,-1,1]


def cell_move():
    global area
    global direction
    labbed_cells = [set()*N for _ in range(N)]
    tmp_area = list([0]*N for _ in range(N))
    tmp_dir = list([0]*N for _ in range(N))
    for i in range(N):
        for j in range(N):
            if area[i][j] != 0:
                nowDir = direction[i][j]
                ni = i + di[nowDir]
                nj = i + dj[nowDir]
                if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
                    tmp_area[ni][nj] = area[i][j]//2
                    if nowDir == 0:
                        tmpDir = 1
                    elif nowDir == 1:
                        tmpDir = 0
                    elif nowDir == 2:
                        tmpDir = 3
                    elif nowDir == 3:
                        tmpDir = 2
                    tmp_dir[ni][nj] = tmpDir
                elif tmp_area[ni][nj] != 0:
                    labbed_cells[ni][nj].add(tmp_area[ni][nj])
                    labbed_cells[ni][nj].add(area[i][j])





for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    area = list([0]*N for _ in range(N))
    direction = list([0]*N for _ in range(N))

    for _ in range(K):
        i, j, nums, direct = map(int, input().split())
        area[i][j] = nums
        direction[i][j] = direct - 1

    while M > 0:
        M -= 1
        pass
