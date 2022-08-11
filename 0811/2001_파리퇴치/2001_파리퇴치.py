import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def killed_fly(arr,M,i,j): #주어진 위치에서 죽일 수 있는 파리의 수 반환
    cnt = 0
    for k in range(i, i + M):
        for l in range(j, j + M):
            cnt += arr[k][l]

    return cnt

for tc in range(1,T+1):
    N, M = map(int, input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N-M+1): #M의 크기만큼 범위의 최대값이 줄어든다
        for j in range(N-M+1):
            #해당 위치에서 죽일 수 있는 파리의 수를 받고 최대 값을 확인한다.
            tmp = killed_fly(arr, M, i, j)
            if tmp > maxV:
                maxV = tmp

    print("#{} {}".format(tc, maxV))

