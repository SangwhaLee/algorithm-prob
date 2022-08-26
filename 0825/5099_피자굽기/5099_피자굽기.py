import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    # N은 화덕의 최대개수, P는 피자의 개수
    N, P = map(int, input().split())
    # 피자의 치즈 양을 보여주는 리스트
    pizzas = list(map(int,input().split()))
    oven = []
    rear = -1

    # 대기중인 피자 중 가장 앞에 번째 피자의 인덱스
    now = 0
    # 먼저 오븐이 가득 찰때까지 피자를 넣어준다. 이떄 피자에 번호를 달아 어떤 피자인지 인지 가능하도록 한다
    while rear < N-1:
        oven.append([now+1,pizzas[now]])
        rear += 1
        now += 1

    # 오븐에 하나의 피자만 남을 때까지 반복한다
    while rear > 0:
        # 오븐에서 먼저 들어간 피자부터 차례대로 확인한다 (Queue)
        tmp = oven.pop(0)
        # print(tmp)
        # 오븐의 치즈양이 2보다 크면 한 번더 들어가고 아니면 꺼낸다
        # 이때 한 번 더 들어가는 피자의 치즈의 양은 절반이 된다
        if tmp[1]//2 > 0:
            tmp[1] = tmp[1]//2
            oven.append(tmp)
        else:
            # 오븐에서 피자를 꺼냈는데 대기중인 피자가 남아있다면 그 피자를 오븐에 넣는다
            if now < P:
                oven.append([now+1, pizzas[now]])
                now += 1
            # 대기중인 피자가 없다면 오븐에 남아있는 피자 개수의 표시를 줄인다
            else:
                rear -= 1

    print("#{} {}".format(tc, oven.pop(0)[0]))