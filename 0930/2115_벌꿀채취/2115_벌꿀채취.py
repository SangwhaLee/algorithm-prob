import sys
sys.stdin = open('sample_input.txt','r')


def check(arr, total, idx, result):
    global max_profit
    if total > C:
        return

    if idx == M and total <= C:
        max_profit = max(max_profit, result)
        return

    for i in range(idx, len(arr)):
        if not check_visited[idx]:
            check_visited[idx] = True
            check(arr, total+ arr[idx], idx+1, result + arr[idx]**2)
            check_visited[idx] = False


def get_honey():
    global max_profit
    max_ans = []
    for i in range(N-1):
        for j in range(N-M+1):
            ans = []
            first_case = []
            second_case = []
            for z in range(M):
                first_case.append(boxes[i][z+j])
            for k in range(i+1, N):
                for l in range(N-M+1):
                    for z in range(M):
                        second_case.append(boxes[k][l+z])
                    # print(first_case)
                    # print(second_case)
                    check(first_case, 0, 0, 0)
                    f_ans = max_profit
                    max_profit = 0
                    check(second_case, 0, 0, 0)
                    s_ans = max_profit
                    max_ans.append(f_ans+s_ans)

    return max(max_ans)



for tc in range(1, int(input())+1):
    N, M, C = map(int,input().split())
    boxes = [list(map(int,input().split())) for _ in range(N)]
    max_profit = 0
    check_visited = [False]*M
    answer = get_honey()
    print(answer)