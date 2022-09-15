import sys
sys.stdin = open('sample_input.txt','r')


def combination(idx, depth):
    global minimum
    # 한 그룹에 들어간 식재료의 개수가 전체 개수의 절반이 되는 것이 종료조건
    if depth == N/2:
        # 각 그룹에 있을 식재료의 시너지 값의 총합을 저장할 변수
        total, total2 = 0, 0
        # 전체 2차원 리스트를 순회하며 두 식재료가 같은 그룹에 속해있는 경우 시너지 값을 총합에 더한다
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    total += table[i][j]
                elif not visited[i] and not visited[j]:
                    total2 += table[i][j]
        minimum = min(minimum, abs(total - total2))
        return

    for i in range(idx, N):
        if not visited[i]:
            # 식재료를 리스트에 표시하여 한 그룹에 속했음을 표시
            visited[i] = True
            combination(i+1, depth+1)
            visited[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    table = list(list(map(int,input().split())) for _ in range(N))
    # 식재료를 두개의 조로 나누기 위해 사용할 리스트
    visited = [False for _ in range(N)]
    minimum = 20001
    combination(0,0)
    print("#{} {}".format(tc, minimum))