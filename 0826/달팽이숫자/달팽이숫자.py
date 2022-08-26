import sys

sys.stdin = open('input.txt','r')
# 기존엔 while문을 이용한 반복문으로 문제를 해결헀었는데 이번엔 재귀를 사용했다
# 코드가 훨씬 깔끔하고 간결하다

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def snail(i,j,step):
    # N과 board는 변하지 않는다
    global N
    global board
    # 재귀 종료 전에 step 값을 저장해줘야 마지막 한칸에 값이 저장된다.
    board[i][j] = step
    if step == N*N:
        return
    step += 1
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
            snail(ni,nj,step)


for tc in range(1, int(input())+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]

    snail(0,0,1)

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()