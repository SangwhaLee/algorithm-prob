import sys
sys.stdin = open('sample_input.txt','r')

# 2차원 리스트에서 최소합을 구하기 위한 함수
def min_sum(si,sj, total):
    # 최종 최소값을 기록하기 위한 변수
    global minimum
    # 만약 현재 위치가 2차원 리스트의 우하단 끝에 도달하게 되면 중단
    if si == N-1 and sj == N-1:
        # 지금까지 더해진 값을 현재까지의 최소값과 비교
        if total < minimum:
            minimum = total
            return

    # 현재 칸에서 우측으로 이동하는 경우
    if sj+1 < N:
        min_sum(si, sj+1, total + board[si][sj+1])
    # 현재 칸에서 좌측으로 이동하는 경우
    if si+1 < N:
        min_sum(si+1, sj, total + board[si+1][sj])


for tc in range(1, int(input())+1):
    N = int(input())
    board = list(list(map(int,input().split())) for _ in range(N))
    minimum = 10000
    min_sum(0, 0, board[0][0])
    print("#{} {}".format(tc, minimum))



