import sys

sys.stdin = open('input.txt','r')


def preorder(a):
    print(a, end=' ')
    if child_l[a] != 0:
        preorder(child_l[a])
    if child_r[a] != 0:
        preorder(child_r[a])


N = int(input())
child_l = [0]*(N+1)          # 왼쪽 자식노드, 오른쪽 자식노들 리스트를 각각 생성
child_r = [0]*(N+1)

edges = list(map(int,input().split()))

for i in range(0,len(edges),2):           # 정렬된 상태로 입력되기 때문에 왼쪽 자식노드 부터 입력되도록 한다.
    if child_l[edges[i]]:
        child_r[edges[i]] = edges[i+1]
    else:
        child_l[edges[i]] = edges[i+1]


preorder(1)