import sys

sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    total, N = map(int, input().split())

    # 최대한 묶음끼리의 수가 같게 만들어야 곱했을때의 최대값이 나타난다.
    # 그렇기 때문에 일단 각각의 묶음의 크기는 기본적으로 총 달란트를 묶음수로 나눈 몫이 된다.
    bundles = [total//N]* N
    answer = 1

    # 만약 총 달란트가 묶음수로 나누어 떨어지면 그대로 곱해서 출력하면 된다.
    # 하지만 그렇지 않을 경우 몫을 구하고 남은 나머지가 0이 될때까지 각 묶음에 하나씩 더하면 된다.
    if total % N:
        cnt = total % N
        step = 0
        while cnt > 0:
            bundles[step%N] += 1
            step += 1
            cnt -= 1
        for bd in bundles:
            answer *= bd
    else:
        for bd in bundles:
            answer *= bd

    print("#{} {}".format(tc, answer))

