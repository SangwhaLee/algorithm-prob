import sys
sys.stdin = open('sample_input.txt','r')
from collections import  deque

# 각각의 연산을 그래프에서 노드를 거쳐가는 것과 동일하게 생각하면 된다.
# 최소한의 연산이라는 것은 목적까지 최소한의 거리로 도착하게 되는 경우랑 같은 것이며 이 경우 bfs가 적합하다
def bfs(start, target):
    que = deque()
    que.append((start,0))
    # 도중 연산 결과가 같은 것이 나오면 중복 연산하지 않도록 하기 위해 set를 사용
    visited = set()
    visited.add(start)
    while que:
        now, cnt = que.popleft()
        for next in (now+1, now-1, now*2, now-10):
            # 연산한 결과가 백만이하이며 같은 연산결과가 현재 존재하지 않을 경우 연산
            if next <= 1e6 and next not in visited:
                visited.add(next)
                que.append((next, cnt+1))
                if next == target:
                    return cnt + 1


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    print("#{} {}".format(tc, bfs(N,M)))