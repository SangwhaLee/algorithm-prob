import sys
sys.stdin = open('input.txt','r')

# DFS를 실행하는 함수
def DFS(v):
    # 노드의 개수는 출발 도착 포함해서 100개이다
    visited = [0]*100
    stack = [0]*100
    top = -1
    # 총경로를 저장할 리스트
    route = []

    # 시작점을 경로에 기록하고 방문체크한다
    route.append(v)
    visited[v] = 1
    while True:
        # 만약 v와 연결된 노드 중에 아직 방문하지 않은 곳이 있다면 그곳으로 이동
        # w는 새로운 v가 되고 경로에 기록하고 방문체크한다
        for w in graph[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[v] = 1
                route.append(v)
                break
        # 현재 v와 연결된 곳은 모두 방문했을 때
        else:
            # 마지막으로 방문한 노드로 되돌아간다 이때 스택을 이용
            if top != -1:
                v = stack[top]
                top -= 1
            # 만약 스택에 다른 값이 없는 경우 이는 더 이상 이동할 곳이 없다는 뜻이다
            else:
                break

    return route


for tc in range(1, 11):
    tnum, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # 간선을 저장할 리스트
    graph = [[] for _ in range(100)]

    # 모든 간선은 하나의 문장으로 주어진다 때문에 이를 분리할 필요가 있다
    # 문장의 짝수 인덱스는 모든 간선의 시작점이고 홀수 인덱스는 도착점이다
    for i in range(0, E*2, 2):
        tmp = []
        for j in range(i, i+2):
            tmp.append(arr[j])
        graph[tmp[0]].append(tmp[1])

    tmp = DFS(0)

    # 만약 반환된 경로안에 99가 존재한다는 것은 어떠한 방법으로든 0에서 99는 이어져있다는 뜻이다.
    if 99 in tmp:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
