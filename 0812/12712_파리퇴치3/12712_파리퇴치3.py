import sys

sys.stdin =open('in1.txt','r',encoding='UTF8')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            plus_style = 0 #+ 모양일때의 잡는 파리의 수
            cross_style = 0# X 모양일 떄 잡는 파리의 수

            k = i #원본인 i,j는 되도록 손상이 가지 않도록 한다
            l = j
            m = 0 #M의 사이즈를 적용하기 위한 변수
            while k + 1 < N and m < M - 1: #중점에서 아래쪽으로 직선범위
                plus_style += arr[k + 1][l]
                k += 1
                m += 1
            k = i
            l = j
            m = 0
            while k - 1 >= 0 and m < M - 1: #중점에서 위쪽으로 직선범위
                plus_style += arr[k - 1][l]
                k -= 1
                m += 1

            k = i
            l = j
            m = 0
            while l + 1 < N and m < M - 1: #중점에서 오른쪽으로 직선범위
                plus_style += arr[k][l + 1]
                l += 1
                m += 1

            k = i
            l = j
            m = 0
            while l - 1 >= 0 and m < M - 1: #중점에서 왼쪽으로 직선범위
                plus_style += arr[k][l-1]
                l -= 1
                m += 1

            plus_style += arr[i][j] #중점도 포함
            if plus_style > maxV:
                maxV = plus_style

            k = i
            l = j
            m = 0
            while k+1 < N and l+1 < N and m<M-1: #중점에서 우하향 대각선 범위
                cross_style += arr[k+1][l+1]
                k += 1
                l += 1
                m += 1
            k = i
            l = j
            m = 0
            while k+1 < N and l-1 >= 0 and m<M-1: #중점에서 좌하향 대각선 범위
                cross_style += arr[k + 1][l - 1]
                k += 1
                l -= 1
                m += 1
            k = i
            l = j
            m = 0
            while k-1 >= 0 and l+1 < N and m<M-1: #중점에서 우상향 대각선 범위
                cross_style += arr[k - 1][l + 1]
                k -= 1
                l += 1
                m += 1
            k = i
            l = j
            m = 0
            while k - 1 >= 0 and l - 1 >= 0 and m<M-1: #중점에서 좌상향 대각선 범위
                cross_style += arr[k-1][l-1]
                k -=1
                l -= 1
                m += 1

            cross_style += arr[i][j] #중점도 포함

            if cross_style > maxV:
                maxV = cross_style

    print("#{} {}".format(tc+1, maxV))