import sys

sys.stdin = open('input.txt','r')

# 한 노드를 통과하면 이어져있는 다른 모든 노드에게 전부 영향을 미치기 때문에 dfs보단 bfs가 어울린다고 생각
# bfs를 통해 다른 노드를 통과하기 위해선 가고자 하는 노드가 모든 선행조건 완료한 상태여야 한다.
def bfs(route, edge, pre, v, n):
    # 통과대기 중인 노드에 대한 큐
    que = []
    que.append(v)
    # 노드 방문록
    visited = [0]*(n+1)
    while que:
        t = que.pop(0)
        # 만약 큐에서 나온 노드가 이미 방문한적이 없다면 사용가능
        if not visited[t]:
            visited[t] = True
            route.append(t)
            for i in edge[t]:
                # 해당 노드를 통과하면 이 노드와 인전한 다른 노드는 이 노드만큼의 선행조건은 이루어진것이다
                pre[i] -= t
                # pre가 0이라는 것은 선행조건이 모두 이루어진것과 같다
                if pre[i] == 0:
                    que.append(i)


for tc in range(1, 11):
    V, E = map(int, input().split())

    arr = list(map(int, input().split()))
    pre = [0]*(V+1)
    edge = [[]*(V+1) for _ in range(V+1)]

    for i in range(0,E*2,2):
        # 각 노드에 대한 선행조건을 추가한다
        pre[arr[i+1]] += arr[i]
        # 간선에 대한 내용을 정리한다
        edge[arr[i]].append(arr[i+1])

    route = []

    start_point = []

    for i in range(1, V+1):
        if pre[i] == 0:
            start_point.append(i)

    for i in start_point:
        bfs(route, edge, pre, i, V)

    print("#{}".format(tc),end=' ')
    for i in route:
        print(i, end=' ')
    print()