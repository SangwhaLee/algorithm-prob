import sys
sys.stdin = open('sample_input.txt','r')

# 순찰을 돌때 1번 칸을 제외한 칸만을 순회하다가 전부 다 순회할 경우 다시 사무실로 돌아온다
def go_office(depth, total, start):
    global minimum
    # 모든 방을 순찰한 경우 마지막 방에서 사무실까지 돌아오는 배터리 소모량도 추가하여 비교한다
    if depth == N-1:
        minimum = min(minimum, total+arr[start][0])
        return

    # 사무실은 한 번 떠나면 모든 방을 순찰할때 까지 돌아오면 안되기 때문에 반복문은 1에서 부터 시작
    for i in range(1, N):
        # 동일한 방으로는 이동할 수 없고, 이미 한 번 들린 방은 갈 필요가 없다
        if arr[start][i] != 0 and not visited[i]:
            visited[i] = True
            go_office(depth+1, total+arr[start][i], i)
            visited[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    visited = [False]*N
    minimum = 1e9

    go_office(0, 0, 0)
    print("#{} {}".format(tc, minimum))

