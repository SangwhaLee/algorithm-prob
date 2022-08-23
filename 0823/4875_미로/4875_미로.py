import sys
sys.stdin = open('sample_input.txt','r')

# 미로에서는 상하좌우로만 움직일 수 있기 때문에 델타탐색을 응용했다
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# DFS와 델타 탐색을 함께 사용했다
def find_way(i,j):
    stack = []
    top = -1

    while True:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 만약 움직이려는 곳에 도착지가 있다면 1을 반환한다
            if N > ni >= 0 and N > nj >= 0 and board[ni][nj] == '3':
                return 1
            # 움직이려는 곳이 판 위의 통로라면 위치 이동을 한다
            if N > ni >= 0 and N > nj >= 0 and board[ni][nj] == '0':
                top += 1
                stack.append([i,j])
                i = ni
                j = nj
                board[i][j] = 1
                break
        # 더 이상 움직일 곳이 없다면 예전에 진행했던 곳으로 돌아간다
        else:
            if top != -1:
                tmp = stack.pop()
                top -= 1
                i = tmp[0]
                j = tmp[1]
            else:
                break
    # 끝날때 까지 3을 못찾았다는 것은 3으로 이동할 수 없는 미로라는 것이다
    return 0

for tc in range(1, int(input())+1):
    # 'error'를 출력하라는 구문이 있어 혹시 모를 예외 상황에 대비한 try구문이다
    try:
        N = int(input())
        board = [list(input()) for _ in range(N)]
        si = 0
        sj = 0

        for i in range(N):
            for j in range(N):
                if board[i][j] == '2':
                    si = i
                    sj = j

        ans = find_way(si, sj)

        print("#{} {}".format(tc, ans))
    except:
        print("#{} error".format(tc))
