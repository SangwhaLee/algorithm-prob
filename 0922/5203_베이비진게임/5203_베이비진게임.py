import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    cards = list(map(int,input().split()))
    p1 = []
    p2 = []
    deck1 = [0] * 10
    deck2 = [0] * 10
    answer = 0
    # 입력받은 값을 순서대로 나눈다
    for i in range(0,len(cards),2):
        p1.append(cards[i])
        p2.append(cards[i+1])

    # 무조건 플레이어1부터 뽑기 때문에 만약 p1이 결과가 나왔다면 승리는 p1의 것이 된다
    for i in range(6):
        deck1[p1[i]] += 1
        deck2[p2[i]] += 1

        if (deck1[p1[i]] >= 3 or
            (p1[i]<=7 and deck1[p1[i]] > 0 and deck1[p1[i]+1] > 0 and deck1[p1[i]+2] > 0) or
            (1<=p1[i]<=8 and deck1[p1[i]] > 0 and deck1[p1[i]-1] > 0 and deck1[p1[i]+1] > 0) or
            (2<=p1[i] and deck1[p1[i]] > 0 and deck1[p1[i]-1] > 0 and deck1[p1[i]-2] > 0)):
            answer = 1
            break

        if (deck2[p2[i]] >= 3 or
            (p2[i]<=7 and deck2[p2[i]] > 0 and deck2[p2[i]+1] > 0 and deck2[p2[i]+2] > 0) or
            (1<=p2[i]<=8 and deck2[p2[i]] > 0 and deck2[p2[i]-1] > 0 and deck2[p2[i]+1] > 0) or
            (2<=p2[i] and deck2[p2[i]] > 0 and deck2[p2[i]-1] > 0 and deck2[p2[i]-2] > 0)):
            answer = 2
            break

    print("#{} {}".format(tc, answer))


