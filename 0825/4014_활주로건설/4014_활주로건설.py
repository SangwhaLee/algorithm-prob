import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    N, x = map(int, input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    row_slope = []
    col_slope = []

    for i in range(N):
        tmp = []
        for j in range(N-1):
            if arr[i][j] != arr[i][j+1]:
                tmp.append()
