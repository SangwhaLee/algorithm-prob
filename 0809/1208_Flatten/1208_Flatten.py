import sys

sys.stdin = open('input.txt','r')



for tc in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for __ in range(dump):
        maxV = 0
        maxIdx = 0
        minV = 101
        minIdx = 0
        for i in range(100):
            if boxes[i] > maxV:
                maxV = boxes[i]
                maxIdx = i
            if boxes[i] < minV:
                minV = boxes[i]
                minIdx = i
        # print("max: {}. min:{}".format(maxV,minV))
        if maxV - minV <= 1:
            # print("#{} {}".format(tc+1, maxV-minV))
            break
        boxes[maxIdx] -= 1
        boxes[minIdx] += 1
    
    maxV = 0
    minV = 101
    for i in range(100):
        if boxes[i] > maxV:
            maxV = boxes[i]
        if boxes[i] < minV:
            minV = boxes[i]
    
    print("#{} {}".format(tc+1, maxV-minV))
        

