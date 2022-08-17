import sys

sys.stdin = open('input.txt','r')

def DFS(v,N):
    visited = [0]*N
    stack = [0]*N
    top = -1

    visited[v] = 1
    print(v+1, end= ' ')
    while True:
        for w in edge[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                print(w+1, end= ' ')
                visited[v] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break


N, E = map(int,input().split())

numbers = list(map(int,input().split()))
#print(numbers)
edge = [[] for _ in range(N)]
#print(edge)

for i in range(0,E*2,2):
    tmp = []
    for j in range(i,i+2):
        tmp.append(numbers[j]-1)
    edge[tmp[0]].append(tmp[1])
    edge[tmp[1]].append(tmp[0])

DFS(0, N)
