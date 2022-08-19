import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N = int(input())

    board = [list(map(int,input().split())) for _ in range(100)]

    '''
    그냥 스택에 2차원 리스트 세로 값을 다 넣고 위에서 부터 꺼내는데 만약 파란색이면
    빨간색이 나올 때까지 계속 뽑고 빨간색이 나오면 교착 수 + 1
    만약 파란색이 나오지 않은 상태에서 빨간색이 나온다 -> 무시
    파란색이 나왔는데 스택 끝까지 빨간색이 안나왔다 -> 무시
    '''
    total = 0
    # 스택의 최대 사이즈를 이미 알고 있기 때무에 스택의 크기를 정해놓고 top만을 조작한다
    stack = [0] * 100
    for i in range(100):
        top = -1
        for j in range(100):
            # 만약 보드위에 자성체가 있다면 스택에 넣어준다
            if board[j][i] != 0:
                top += 1
                stack[top] = board[j][i]

        # 스택이 빌 때까지 반복
        while top != -1:
            # 파란색이 나오면 빨간색이 나올때까지 계속 스택에서 뽑는다
            if stack[top] == 2:
                # 스택의 크기를 미리 선언해놨기 때문에 0이 하나의 값으로 인식될 수 있다
                while stack[top] != 1 and stack[top] != 0:
                    top -= 1
                if top != -1:
                    total += 1
            else:
                top -= 1

    print("#{} {}".format(tc,total))