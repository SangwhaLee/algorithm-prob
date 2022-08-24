import sys
sys.stdin = open('input.txt','r')

def bfs(edge, v, N):
    # 해당 노드를 방문했는지 확인하기 위한 리스트 
    visited = [0]*(N+1)
    # 큐를 통해 인접리스트를 인지
    queue = []
    # 시작점을 일단 큐에 넣는다
    queue.append(v)
    # 시작점은 방문한 것으로 한다
    visited[v] = 1

    # 큐에서 한 값을 꺼내고 그 값의 인접 노드 중 아직 방문한적이 없는
    # 노드를 큐에 저장한다 그리고 해당 노드에 방문록에 전 노드의 방문록에 대한 값에서 1을 더한다
    # 이 과정을 통해 해당 노드가 시작점으로 부터 얼마나 떨어져있는지를 알 수 있다
    # 위의 과정은 큐가 빌 때까지 계속 반복한다.
    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in edge[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[i] + 1

N, M = map(int, input().split())

# 간선에 대한 데이터를 일렬로 입력받는다
arr = list(map(int,input().split()))

# arr에서 간선의 시작과 끝을 따로 나누어 2차원 리스트로 저장 
edge = [[]*(N+1) for _ in range(N+1)]

for i in range(0,M*2,2):
    edge[arr[i]].append(arr[i+1])

bfs(edge,1,N)

