import sys
sys.stdin = open('sample_input.txt','r')

'''
이진 최소힙을 만들어 입력받은 값을 올바른 순서대로 정리하는 문제
'''

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0]
    node = list(map(int,input().split()))
    now = 0

    # 입력받은 데이터를 tree에 하나하나 추가하고 그 과정에서 자식 노드가 부모 노드보다 커지는 경우 서로 교환한다.
    for i in range(len(node)):
        tree.append(node[i])
        # now는 현재 추가된 노드의 위치 (노드 번호)를 나타낸다
        now += 1
        # 자신이 전체 트리의 루트 노드가 아니라면
        if now // 2 != 0:
            child = now
            # 자신의 부모노드의 값이 자신보다 클 경우 둘을 교환
            while tree[child // 2] > tree[child]:
                tree[child // 2], tree[child] = tree[child], tree[child // 2]
                child = child // 2

    idx = len(node)//2
    total = 0
    # 마지막 노드의 부모노드들의 합
    while idx > 0:
        total += tree[idx]
        idx //= 2

    print("#{} {}".format(tc, total))