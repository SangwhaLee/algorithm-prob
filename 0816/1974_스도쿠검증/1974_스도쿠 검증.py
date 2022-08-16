import sys
sys.stdin = open('input.txt','r')

# 스도쿠 검사를 위한 함수
def checkSudoku(sudoku):
    for i in range(9):
        # 검사를 위한 배열을 만들어준다
        v_check = [0] * 10
        h_check = [0] * 10
        for j in range(9):
            # 만약 현재 위치에 있는 값이 이미 같은 수직선상에 존재한다면
            if v_check[sudoku[i][j]]:
                return 0
            # 만약 현재 위치에 있는 값이 이미 같은 가로선상에 존재한다면
            if h_check[sudoku[j][i]]:
                return 0
            # 세로, 가로 선상에 해당 숫자가 없을 경우 기록
            v_check[sudoku[i][j]] = 1
            h_check[sudoku[j][i]] = 1
            # 각 상자의 기준이 되는 기준점의 경우
            if i%3 ==0 and j%3 ==0:
                # 작은 상자 검사를 위한 배열
                s_check = [0]*10
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if s_check[sudoku[k][l]]:
                            return 0
                        s_check[sudoku[k][l]] = 1

    return 1

for tc in range(1,int(input())+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]

    ans = checkSudoku(sudoku)
    print("#{} {}".format(tc, ans))
