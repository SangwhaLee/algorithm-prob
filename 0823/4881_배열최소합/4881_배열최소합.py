# import sys
# sys.stdin = open('sample_input.txt','r')

def backtrack(a, k, N):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES

    if k == N:
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a, k, N, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, N)

def construct_candidates(a, k, N, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates =0
    for i in range(1, N+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    return ncandidates



for tc in range(1, int(input())+1):
    N = int(input())

    #arr = [list(map(int, input().split())) for _ in range(N)]

    MAXCANDIDATES = 2
    NMAX = 4
    a = [0] * NMAX
    backtrack(a, 0, 3)
