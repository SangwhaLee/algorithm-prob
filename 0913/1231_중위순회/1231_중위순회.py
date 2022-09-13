import sys
sys.stdin = open('input.txt','r')


def in_order(node):
    if node <= N:
        in_order(node*2)                  # 왼쪽 자식노드의 인덱스 값은 부모의 *2
        print(tree[node], end='')         # 중위 순회이기 때문에 두번째로 배치
        in_order(node*2 + 1)              # 오른쪽 자식노드의 인덱스 값은 부모의 *2 + 1


for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)                      # 배열을 이용해 트리를 저장

    for i in range(N):
        tmp = list(input().split())
        tree[i+1] = tmp[1]               # 다른거 상관없이 배열의 위치에 해당 되는 데이터만 저장

    print("#{}".format(tc), end=' ')
    in_order(1)
    print()
