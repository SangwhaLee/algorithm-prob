import sys
sys.stdin = open('input.txt','r')

# 각 상자의 정보를 정렬하기 위한 버블 정렬 함수
# 각 상자의 크기를 비교해 오름차순으로 정렬하지만 크기가 같은 상자는 행의 크기가
def bubble_sort(arr, N):
    for i in range(N-1, -1, -1):
        for j in range(1,i+1):
            if arr[j][2] < arr[j-1][2]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            elif arr[j][2] == arr[j-1][2]:
                if arr[j][0] < arr[j-1][0]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]


for tc in range(1, int(input())+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    information = []

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] != 0:
                row_cnt = 0
                col_cnt = 0
                ni = i
                nj = j
                while nj < N and arr[ni][nj] != 0:
                    row_cnt += 1
                    nj += 1
                nj = j
                while ni < N and arr[ni][nj] != 0:
                    col_cnt += 1
                    ni += 1
                for k in range(i, i+col_cnt):
                    for l in range(j, j+row_cnt):
                        visited[k][l] = 1
                information.append((col_cnt, row_cnt, col_cnt*row_cnt))

    bubble_sort(information, len(information))
    print("#{} {}".format(tc, len(information)), end=' ')
    for i in range(len(information)):
        print(information[i][0], end=' ')
        print(information[i][1], end=' ')
    print()





