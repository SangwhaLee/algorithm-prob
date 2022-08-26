import sys
sys.stdin = open('sample_input.txt','r')

# 너비 우선 탐색을 진행하면서 도착점까지의 거리를 확인할 수 있도록 한다
def bfs(V, S, G):
    # 각 노드들이 시작점으로 부터 얼마나 떨어져있는가를 알 수 있는 리스트
    visited = [0]*(V+1)
    que = []
    que.append(S)
    visited[S] = 0
    while que:
        t = que.pop(0)
        for k in edge[t]:
            if k == G:
                return visited[t]+1
            if not visited[k]:
                que.append(k)
                visited[k] = visited[t] + 1

    return 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    edge = [[]*(V+1) for _ in range(V+1)]

    # 각 간선은 방향성이 없는 양방향 간선이기 때문에 두 경우 모두 추가해주는 것이 조다
    for i in range(E):
        sn, en = map(int, input().split())
        edge[sn].append(en)
        edge[en].append(sn)

    S, G = map(int, input().split())

    ans = bfs(V, S, G)

    print("#{} {}".format(tc, ans))