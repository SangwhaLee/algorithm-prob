import sys
sys.stdin = open('sample_input.txt','r')

# DFS 함수
def DFS(v):
    # 스택을 이용할 것이기 때문에 top과 stack 선언
    top = -1
    # 해당 노드를 온적이 있는지를 확인
    visited = [0] * (V + 1)
    stack = [0] * (V+1)
    # 시작점을 방문체크
    visited[v] = 1
    # 어디를 들렸는지 저장할 리스트
    route = []

    route.append(v)
    while True:
        # 만약 v와 연결된 아직 방문하지 않은 노드가 존재한다면
        for w in graph[v]:
            # 해당 노드를 새로운 v로 만들고 기존의 v는 스택에 저장
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                route.append(w)
                visited[v] = 1
                break
        # 만약 v와 연결된 노드가 이제 존재하지 않는다면 마지막으로 방문한 노드로 돌아간다
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            # 만약 스택이 비어있다면 더이상 방문할 수 있는 노드가 없다는 뜻이므로 순환을 끝낸다
            else:
                break

    return route

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for i in range(E):
        tmp = list(map(int,input().split()))
        graph[tmp[0]].append(tmp[1])


    #print(graph)
    S, G = map(int,input().split())
    #print(S,G)

    tmp = DFS(S)

    if G in tmp:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))