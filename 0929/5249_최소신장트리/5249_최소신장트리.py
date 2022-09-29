import sys
sys.stdin = open('sample_input.txt','r')


def find_set(x):
    if x != root[x]:
        root[x] = find_set(root[x])
    return root[x]


def union(x,y):
    link(find_set(x), find_set(y))


def link(x,y):
    if rank[x] > rank[y]:
        root[y] = x
    else:
        root[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def kruskal():
    a = 0

    for i in range(E):
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            a += edges[i][2]
            union(edges[i][0], edges[i][1])

    return a


for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    edges = []
    for _ in range(E):
        n1, n2, t = map(int,input().split())
        edges.append((n1,n2,t))

    edges.sort(key = lambda x: x[2])
    root = [i for i in range(V+1)]
    rank = [0 for _ in range(V+1)]

    total = kruskal()

    print("#{} {}".format(tc, total))

