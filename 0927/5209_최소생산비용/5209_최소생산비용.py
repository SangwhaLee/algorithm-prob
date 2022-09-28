import sys
sys.stdin = open('sample_input.txt','r')


def work_house(depth, total):
    global minimum
    if depth == N:
        minimum = min(total, minimum)

    if total >= minimum:
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            work_house(depth+1, total+board[depth][i])
            visit[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    board = list(list(map(int, input().split())) for _ in range(N))
    visit = [False]*N
    minimum = 1e9

    work_house(0, 0)

    print("#{} {}".format(tc, minimum))