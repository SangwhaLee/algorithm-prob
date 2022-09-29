import sys
sys.stdin = open('sample_input.txt','r')


def dijkstra(s):
    node_set = {s}

    for i in range(1,N+1):
        dis[i] = edges[s][i]

    while len(node_set) < N+1:
        small = float('inf')
        small_idx = 0
        for i in range(1,N+1):
            if dis[i] < small and i not in node_set:
                small = dis[i]
                small_idx = i
        node_set.add(small_idx)
        w = small_idx

        for i in range(1,N+1):
            if edges[w][i] != float('inf'):
                dis[i] = min(dis[i], dis[w] + edges[w][i])


for tc in range(1, int(input())+1):
    N, E = map(int,input().split())
    edges = [[float('inf')]*(N+1) for _ in range(N+1)]

    for i in range(E):
        s, e, t = map(int,input().split())
        edges[s][e] = t

    dis = [0]*(N+1)

    dijkstra(0)

    print("#{} {}".format(tc,dis[N]))