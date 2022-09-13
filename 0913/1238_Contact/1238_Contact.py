import sys
from collections import deque

sys.stdin = open('input.txt','r')


def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        tmp = que.popleft()
        for ed in edges[tmp]:
            if visited[ed] == 0:
                visited[ed] = visited[tmp] + 1
                que.append(ed)


for tc in range(1, 11):
    length, start = map(int,input().split())
    data = list(map(int,input().split()))
    top_node = max(data)                             # 입력받은 간선 정보에서 가장 큰 노드의 크기를 확인한다
    edges = [[] for _ in range(top_node+1)]          # 노드간 간선 정보를 정리하기 위한 리스트
    visited = [0]*(top_node+1)                       # 언제 방문했는지를 확인하기 위한 리스트

    for i in range(0,length, 2):                     # 같은 간선 정보도 존재하기 때문에 중복저장 되지 않도록 한다.
        if data[i+1] not in edges[data[i]]:
            edges[data[i]].append(data[i+1])

    bfs(start)

    maximum = max(visited)                           # 어느정도의 거리가 가장 먼 거리인지 확인
    answer = []
    for i in range(len(visited)):                    # 가장 먼거리에 있는 노드들의 번호를 저장
        if visited[i] == maximum:
            answer.append(i)

    print("#{} {}".format(tc, max(answer)))         # 저장된 가장 먼 노드 중 가장 번호가 큰 것을 출력