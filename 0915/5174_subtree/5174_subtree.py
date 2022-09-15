import sys
sys.stdin = open('sample_input.txt','r')

'''
입력받은 노드를 루트로 하는 서브트리의 총 노드 개수를 구하는 문제
'''

# 중위 순회를 돌며 노드의 개수를 센다
def in_order(N):
    global cnt
    if child_l[N] != 0:
        in_order(child_l[N])
    cnt += 1
    if child_r[N] != 0:
        in_order(child_r[N])


for tc in range(1, int(input())+1):
    edge_num, N = map(int,input().split())
    data = list(map(int,input().split()))

    # 총 노드의 개수에 맞게 자식 노드를 표현할 리스트를 만든다. 하나는 왼쪽자식 나머지는 오른쪽자식이 된다
    child_l = [0]*(edge_num+2)
    child_r = [0]*(edge_num+2)

    # 만약 왼쪽노드 리스트의 위치에 부모노드가 정해져 있는경우 오른쪽자식노드 리스트에 등록한다.
    # 정해져 있지 않으면 왼쪽자식노드 리스트에 등록한다.
    for i in range(0,edge_num*2,2):
        if child_l[data[i]] == 0:
            child_l[data[i]] = data[i+1]
        else:
            child_r[data[i]] = data[i+1]

    now = N
    cnt = 0
    in_order(N)

    print("#{} {}".format(tc, cnt))