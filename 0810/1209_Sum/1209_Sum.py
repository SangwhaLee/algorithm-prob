import sys

sys.stdin = open('input.txt','r')

for tc in range(10):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    d1_total = 0
    d2_total = 0
    max_total = 0
    for i in range(100):
        col_total = 0 #col, row는 i의 값이 바뀔때마다 초기화 필요
        row_total = 0
        for j in range(100):
            col_total += arr[i][j] #행을 기준으로 하나의 열에 있는 수를 더한 값
            row_total += arr[j][i] #열을 기준으로 하나의 행에 있는 수를 더한 값
        if max_total < col_total:
            max_total = col_total
        if max_total < row_total:
            max_total = row_total
        d1_total += arr[i][i] #우하향 대각선에 있는 값들은 i,j의 값이 같은 경우
        d2_total += arr[i][99-i]#우상향 대각선에 있는 값들은 j의 값이 99-i의 결과

    if d1_total > max_total:
        max_total = d1_total
    if d2_total > max_total:
        max_total = d2_total

    print("#{} {}".format(tc+1, max_total))