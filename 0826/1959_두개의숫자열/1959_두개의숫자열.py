import sys
sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        maxV =0
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += A[j]*B[i+j]
            if total > maxV:
                maxV = total
    else:
        maxV = 0
        for i in range(N - M + 1):
            total = 0
            for j in range(M):
                total += A[i+j] * B[j]
            if total > maxV:
                maxV = total

    print("#{} {}".format(tc, maxV))
