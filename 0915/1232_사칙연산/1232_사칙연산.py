import sys
sys.stdin = open('input.txt','r')


def in_order(n):
    if n <= N:
        # 노드의 값이 연산자인 경우에 좌측 서브트리의 연산 결과와 우측 서브트리의 연산 결과를 사용해 연산
        if not tree[n].isdigit():
            if tree[n] == '+':
                return in_order(edge[n][0]) + in_order(edge[n][1])
            elif tree[n] == '-':
                return in_order(edge[n][0]) - in_order(edge[n][1])
            elif tree[n] == '*':
                return in_order(edge[n][0]) * in_order(edge[n][1])
            elif tree[n] == '/':
                return in_order(edge[n][0]) / in_order(edge[n][1])
        else:
            return int(tree[n])


for tc in range(1, 11):
    N = int(input())
    # 입력받은 데이터를 저장하기 위한 트리 배열
    tree = [0]*(N+1)
    # 노드끼리 연결을 저장하기 위한 인접리스트
    edge = [[] for _ in range(N+1)]

    for i in range(N):
        tmp = list(input().split())
        # 연산자 정수 상관없이 tree에 값을 저장
        tree[int(tmp[0])] = tmp[1]
        # 자식 노드의 번호를 입력받은 경우 인접리스트에 저장
        if not tmp[1].isdigit():
            edge[int(tmp[0])].append(int(tmp[2]))
            edge[int(tmp[0])].append(int(tmp[3]))

    # print(tree)
    print("#{} {}".format(tc,int(in_order(1))))
