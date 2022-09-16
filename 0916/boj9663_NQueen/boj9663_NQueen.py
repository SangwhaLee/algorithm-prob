# 퀸을 놓는 함수
def Queen(depth):
    global cnt
    # 마지막으로 퀸을 놓은 위치가 N번째 칸이라면 목표를 달성한 것
    if depth == N:
        cnt += 1
        return

    # 현재 높이의 칸에서 퀸이 가로로 어느 칸에 놓을지 한 번씩 다 놓기 위한 반복문
    for i in range(N):
        # 현재 depth 높이의 퀸이 가로로 i번째 칸에 넣었다는 뜻
        visited[depth] = i
        if possibility(depth):
            Queen(depth + 1)

# 놓아진 퀸의 위치가 올바른지를 확인하는 함수
def possibility(column):
    # 퀸은 우리가 맨 위칸에서 부터 한칸씩 아래로 내려오면서 놓는다는 것을 가정한 상태
    # 현재 검증받는 칸보다 높이 있는 칸들을 확인하는 반복문
    for i in range(column):
        # 검증받는 칸이 놓은 가로 위치가 이미 위쪽에서 누가 사용하고 있는 경우
        if visited[column] == visited[i]:
            return False

        # 위쪽에 존재하는 퀸과의 x값의 차이, y값의 차이가 둘 다 같은 경우 동일 대각선상에 위치하고 있다는 뜻
        elif abs(column - i) == abs(visited[column] - visited[i]):
            return False

    return True



N = int(input())
cnt = 0
# 각 퀸이 현재 어느 칸에 놓였는지를 확인하기 위한 리스트
visited = [0] * N
Queen(0)

print(cnt)
