import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    # 트리의 배열에서 주어진 위치에 맞게 값을 저장
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    # 리프 노드는 리스트의 끝에 위치했기 때문에 리스트를 역으로 돌며 자신의 부모노드에 자신의 값을 누적합하면 된다.
    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print("#{} {}".format(tc, tree[L]))