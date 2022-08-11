import sys

sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split())) #정렬할 숫자 입력

    # 선택 정렬을 통해 정렬
    for i in range(N-1):
        #가장 앞의 값을 기준으로 둔다
        minV = arr[i]
        for j in range(i+1,N):
            #지금 기준보다 작은 값이 나타날 경우 교환
            if arr[j] < minV:
                minV = arr[j]
                arr[i], arr[j] = arr[j], arr[i]

    print("#{}".format(tc), end=' ')
    for i in range(N):
        if i == N-1:
            print(arr[i])
        else:
            print(arr[i], end=' ')