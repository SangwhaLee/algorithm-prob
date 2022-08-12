import sys

sys.stdin = open('input1.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                k = j
                cnt = 1
                while k+1<M and arr[i][k+1] == 1:
                    k += 1
                    cnt += 1
                if cnt > maxV:
                    maxV = cnt

                k = i
                cnt = 1
                while k+1 < N and arr[k+1][j] == 1:
                    k += 1
                    cnt += 1
                if cnt > maxV:
                    maxV = cnt

    print("#{} {}".format(tc, maxV))
