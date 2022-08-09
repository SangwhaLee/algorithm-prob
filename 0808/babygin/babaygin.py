import sys

sys.stdin = open('sample_input.txt','r')

N = int(input())

cards = []

for i in range(N):
    cards.append(list(input()))

i=0 
for card in cards:
    result = [0]*12
    for number in card:
        result[int(number)] +=1
    
    k = 0
    tri= run = 0
    # print(result)
    while k < 10:
        if result[k] >= 3:
            result[k] -= 3
            tri += 1
            continue
        if result[k] >= 1 and result[k+1] >= 1 and result[k+2] >= 1:
            result[k] -=1
            result[k+1] -= 1
            result[k+2] -= 1
            run += 1
            continue
        k += 1
    if run+tri == 2: print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i+1))
    i += 1