import sys
sys.stdin = open('input.txt','r')

from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

# bfs를 통해 가장 많이 이동한 방의 길이를 알아낸다
def bfs(si,sj):
    que = deque()
    que.append((si,sj))
    # 해당 문제에서 방을 이동하기 위한 조건은 지금 방보다 다음 방이 정확히 1 클것
    # 그리고 같은 번호는 두 개 존재하지 않기 때문에 이미 지나온 길을 다시 돌아가거나
    # 길이 갈라져서 갈 위험을 계산할 필요가 없다.
    step = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if arr[ni][nj] - arr[i][j] == 1:
                que.append((ni,nj))
                step += 1

    return step

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    max_ans = 0
    ans_idx = [0]*2
    ans_room = []

    # 2중 for문으로 모든 시작점에서 한 번씩 bfs를 실행해보고 가장 값이 높은 위치들을 리스트에 저장
    # 그 중 방번호가 가장 작은것을 골라 출력
    for i in range(N):
        for j in range(N):
            temp = bfs(i, j)
            if max_ans < temp:
                ans_room.clear()
                ans_room.append(arr[i][j])
                max_ans = temp
            elif max_ans == temp:
                ans_room.append(arr[i][j])

    print("#{} {} {}".format(tc, min(ans_room), max_ans))