import sys

sys.stdin = open('input.txt','r',encoding='UTF8')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    carrots = list(map(int,input().split()))
    cnt = 1
    maxV = 1

    for i in range(1,N):
        if carrots[i] > carrots[i-1]: #전당근과 비교해서 더 크면 cnt를 올린다
            cnt += 1
            if cnt > maxV: #만약 지금 카운트가 여태의 최대보다 크면 최대값 차지
                maxV = cnt
        else:
            cnt = 1

    print("#{} {}".format(tc, maxV))