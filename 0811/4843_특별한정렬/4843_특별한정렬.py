import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = []

    for i in range(N-1): #선택 정렬을 통해 리스트 arr 정렬
        minV = arr[i]
        minIdx = i
        for j in range(i+1,N):
            if arr[j] < minV:
                minV = arr[j]
                arr[i], arr[j] = arr[j], arr[i]

    #정렬된 리스트의 양끝에서 하나씩 순차적으로 가져오는 것으로
    #문제에서 원하는 모습의 리스트 생성
    left = 0
    right = N-1
    while left < right:
        result.append(arr[right])
        right -= 1
        result.append(arr[left])
        left += 1
    if N%2: #전체 길이가 홀수인 경우 가운데 하나의 수가 남기에 따로 처리
        result.append(arr[left])

    print("#{}".format(tc), end=' ')
    for i in range(10):
        if i == 9:
            print(result[i])
        else:
            print(result[i], end= ' ')