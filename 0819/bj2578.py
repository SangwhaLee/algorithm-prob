import sys

'''
bingo-check에 숫자를 넣으면 해당 값이 board 내에 있는 지를 확인하고 같은 위치의 check에
1을 넣는다. check가 된다면 그 이후에 해당 위치에서의 행과 열의 총합을 확인하고 값이 5인 경우 cnt를 증가
'''


def bingo_check(N):
    global bingo_cnt
    global check
    nflag = True
    ni = 0
    nj = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == N:
                check[i][j] = 1
                ni = i
                nj = j
                nflag = False
                break
        if not nflag:
            break

    # 저장해놓은 위치 기준으로 행과 열의 합을 구한다
    # 조건이 된다면 대각선의 합도 구한다
    col_sum = 0
    row_sum = 0
    lDiagnol_sum = 0
    rDiagnol_sum = 0
    for i in range(5):
        col_sum += check[i][nj]
        row_sum += check[ni][i]
    if ni == nj:
        for i in range(5):
            lDiagnol_sum += check[i][i]
    if nj == 4 - ni:
        for i in range(5):
            rDiagnol_sum += check[i][4 - i]

    # 구한 합의 값이 5일때 그 줄에 빙고를 달성했다고 판단해 빙고 카운트롤 올린다
    if col_sum == 5:
        bingo_cnt += 1
    if row_sum == 5:
        bingo_cnt += 1
    if lDiagnol_sum == 5:
        bingo_cnt += 1
    if rDiagnol_sum == 5:
        bingo_cnt += 1


board = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]

check = [[0]*5 for _ in range(5)]
bingo_cnt = 0
cnt = 0
flag = True

numbers = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        bingo_check(numbers[i][j])
        cnt += 1
        if bingo_cnt >= 3:
            flag = False
            break

    if not flag:
        break

print(cnt)

