import sys

sys.stdin = open('input.txt','r')

def snail_box(arr, i, j, N, step):
    if N == 1: #N이 1인 경우 들어가는 값은 1하나로 함수 밖에서 이미 처리됐음
        return
    #기본적인 진행상황은 오른쪽으로 무한히 가다가 종료조건이 달성되면 그 다음엔 아래로
    #그 다음엔 왼쪽 그 다음엔 위쪽으로 꺾이면서 움직인다
    while step <= N**2:
        while (j+1 < N) and (arr[i][j+1] == 0): #리스트의 끝까지 가거나 도중에 이미 다른 값이 입력되어있는 경우
            arr[i][j+1] = step
            j += 1
            step += 1

        while (i+1 < N) and (arr[i+1][j] == 0): #리스트의 끝까지 가거나 도중에 이미 다른 값이 입력되어있는 경우
            arr[i+1][j] = step
            i += 1
            step += 1

        while (j-1 >= 0) and (arr[i][j-1] == 0): #리스트의 끝까지 가거나 도중에 이미 다른 값이 입력되어있는 경우
            arr[i][j-1] = step
            j -= 1
            step += 1

        while (i-1 >= 0) and (arr[i-1][j] == 0): #리스트의 끝까지 가거나 도중에 이미 다른 값이 입력되어있는 경우
            arr[i-1][j] = step
            i -= 1
            step += 1

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)] #먼저 N의 크기에 맞게 빈리스트 생성
    i = 0
    j = 0 #시작 좌표 i,j
    cnt = 2 #함수에서는 두번 째 칸부터 값을 채워넣는다
    arr[i][j] = 1 #어떤 수가 나오던 시작점은 동일하므로 먼저 처리한다

    snail_box(arr, i, j, N, cnt)

    print(arr)


