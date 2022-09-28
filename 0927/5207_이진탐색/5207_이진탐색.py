import sys
sys.stdin = open('sample_input.txt','r')


def binary_search(target, l, r, idx):
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == target:
            return True
        elif A[mid] < target:
            l = mid + 1
            if not check[idx][1]:
                check[idx][1] = True
                check[idx][0] = False
            else:
                return False
        else:
            r = mid - 1
            if not check[idx][0]:
                check[idx][0] = True
                check[idx][1] = False
            else:
                return False
    return False


for tc in range(1,int(input())+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    check = [[False, False] for _ in range(M)]
    cnt = 0

    for i in range(M):
        if binary_search(B[i], 0, N-1, i):
            cnt += 1

    print("#{} {}".format(tc, cnt))

