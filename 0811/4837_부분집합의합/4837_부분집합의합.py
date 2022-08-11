import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())
arr = list(i for i in range(1,13))

for tc in range(T):
    N, K = map(int,input().split())
    cnt = 0

    for i in range(1<<12):
        tmp = []
        length = 0
        total = 0
        for j in range(12): #부분집합 구성요소를 tmp리스트에 저장
            if i & (1<<j):
                tmp.append(arr[j])

        #리스트에 저장된 값의 총합과 리스트의 길이가 K, N에 동일한 경우
        for j in tmp:
            total += j
            length += 1

        if total == K and length == N:
            cnt += 1

    print("#{} {}".format(tc+1, cnt))