import sys
sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    maximum = -1e9

    for i in range(M-N+1):
        total = 0
        for j in range(N):
            total += A[j] * B[i+j]
        maximum = max(total, maximum)

    print("#{} {}".format(tc, maximum))