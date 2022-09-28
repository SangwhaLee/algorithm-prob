import sys
sys.stdin = open('input.txt','r')


def dfs(depth, result):
    global maximum
    if depth == N:
        maximum = max(result, maximum)
        return

    if result <= maximum:
        return

    for i in range(N):
        if not work[i]:
            work[i] = True
            new_result = result*board[depth][i]*0.01
            dfs(depth+1, new_result)
            work[i] = False


for tc in range(1, int(input())+1):
    N = int(input())

    board = list(list(map(int,input().split())) for _ in range(N))
    work = [False]*N

    maximum = -1e9

    dfs(0, 1)

    print("#{} {}".format(tc, format(maximum*100, ".6f")))