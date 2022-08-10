import sys

sys.stdin = open('input.txt', 'r')

def sum_around(arr, i, j):
    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    origin = arr[i][j] #기준 위치의 값
    total = 0

    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 4 >= ni >= 0 and 4 >= nj >= 0: #ni, nj가 리스트의 범위를 벗어나지 않는 조건에서
            if arr[ni][nj] > origin: #절대값 내장함수 abs()를 사용하지 않기 위한 조건문
                total += arr[ni][nj] - origin
            else:
                total += origin - arr[ni][nj]

    return total


T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(n):
            total += sum_around(arr, i, j)

    print("#{} {}".format(tc+1, total))