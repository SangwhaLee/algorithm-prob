import sys

sys.stdin = open('sample_input.txt', 'r')

N = int(input())

for tc in range(N):
    width = int(input())
    boxes = list(map(int, input().split()))

    offset = 0 
    base = width
    maxDrop = 0

    for i in range(width):
        p_hight = 0
        nowDrop = 0
        for j in range(width):
            if boxes[j] >= boxes[i]:
                p_hight += 1
        
        nowDrop = base - offset - p_hight
        
        if nowDrop > maxDrop:
            maxDrop = nowDrop
        
        offset += 1
    
    print("#{} {}".format(tc+1, maxDrop))


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
