import sys
sys.stdin = open('sample_input.txt','r')

# 트리를 만들기 위한 함수
# 만약 노드의 왼쪽 자식 노드가 존재한다면 존재하지 않을 때까지 계속 내려간다.
# 더 이상 순회할 왼쪽 자식 노드가 존재하지 않을 경우 노드에 현재 step값을 저장하고 step을 하나 증가한다
# 그 후 오른쪽 자식노드를 순회한다.
def make_tree(idx):
    global step
    if idx <= N:
        make_tree(idx*2)
        tree[idx] = step
        step += 1
        make_tree(idx*2+1)


for tc in range(1,int(input())+1):
    N = int(input())
    tree = [0]*(N+1)
    # 시작 노드 번호는 1번이다
    step = 1
    make_tree(1)

    print("#{} {} {}".format(tc,tree[1], tree[N//2]))


