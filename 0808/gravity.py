N = int(input())

for i in range(N):
    length = int(input())
    result = [[0]*length]*length
    arr = list(map(int,input().split()))
    # print(result)

    step = 0
    while step < length:
        for i in range(arr[step]):
            result[step][i] = 1
        step += 1
    print(result)

    maxDrop = 0

    # for i in range(length):
    #     now = 
    #     while 

    print(maxDrop)

# # 카운트 정렬
# tmp = [0] * N
# c = [0]*101 #0부터 100까지 숫자 개수, 인덱스가 100까지 있어야함
# for i in range(N):
#     c[arr[i]] += 1


# for j in range(1, 101):
#     c[j] += c[j-1]

# for i in range(N-1, -1, -1):
#     c[arr[i]] -= 1
#     tmp[c[arr[i]]] = arr[i]


# # 거품정렬
# for i in range(N-1,0,-1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
