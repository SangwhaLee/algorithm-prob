import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    container = list(map(int,input().split()))
    truck = list(map(int, input().split()))
    visited = [False]*N
    container.sort(reverse=True)
    truck.sort(reverse=True)
    total = 0
    for i in range(M):
        if container == [] or container[-1] > truck[i]:
            break
        for j in range(len(container)):
            if container[j] <= truck[i] and not visited[j]:
                total += container[j]
                visited[j] = True
                break

    print("#{} {}".format(tc, total))
