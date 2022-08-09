import sys

sys.stdin = open('sample_input.txt','r')

N = int(input())

for i in range(1,N+1):
    number = int(input())
    cards = [0]*10

#숫자가 0으로 시작하는 경우 바로 int()를 쓰면 0이 사라지는 경우를 대비
    hand = list(input()) 
    # print(hand)
    for j in hand:
#cards의 index로 들어갈때 정수화
        cards[int(j)] += 1
    
    maxV = cards[0]
    maxIdx = 0
    for j in range(10):
        if cards[j] >= maxV:
            maxV = cards[j]
            maxIdx = j
    
    print('#{} {} {}'.format(i,maxIdx, maxV))