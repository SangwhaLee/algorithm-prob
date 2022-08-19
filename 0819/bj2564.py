width, height = map(int,input().split())

st_num = int(input())
stores = []

for i in range(st_num):
    tmp = list(map(int,input().split()))
    stores.append(tmp)

now = list(map(int,input().split()))

total = 0

'''
동근이의 경비회사의 방향 = 1 , 가게방향이 3,4이면 now[1]+stroes[i][2],
2면 now[i]랑 width - now[i]랑 비교해서 작은 값 + height + min(stores[i][1], width - stores[i][1])
'''

for i in range(st_num):
    # 동근이 회사의 방향에 따라 거리 계산법이 달라진다
    if now[0] == 1:
        # 자신과 같은 방향에 있는 가게
        if stores[i][0] == now[0]:
            total += abs(now[1] - stores[i][1])
        # 서쪽 방면에 있는 가게
        elif stores[i][0] == 3:
            total += now[1]+stores[i][1]
        # 동쪽 방면에 있는 가게
        elif stores[i][0] == 4:
            total += (width-now[1]) + stores[i][1]
        # 남쪽 방면에 있는 가게
        else:
            total += height + min(now[1]+stores[i][1], width-now[1] + width-stores[i][1])
    # 회사의 방향이 남쪽
    elif now[0] == 2:
        if stores[i][0] == now[0]:
            total += abs(now[1] - stores[i][1])
        elif stores[i][0] == 3:
            total += now[1]+(height-stores[i][1])
        elif stores[i][0] == 4:
            total += (width-now[1]) + (height-stores[i][1])
        else:
            total += height + min(now[1]+stores[i][1], width-now[1] + width-stores[i][1])
    # 회사의 방향이 서쪽
    elif now[0] == 3:
        if stores[i][0] == now[0]:
            total += abs(now[1] - stores[i][1])
        elif stores[i][0] == 1:
            total += (now[1] + stores[i][1])
        elif stores[i][0] == 2:
            total += (height-now[1]) + stores[i][1]
        else:
            total += width + min(now[1]+stores[i][1], height-now[1] + height-stores[i][1])
    # 회사의 방향이 동쪽
    else:
        if stores[i][0] == now[0]:
            total += abs(now[1] - stores[i][1])
        elif stores[i][0] == 1:
            total += (now[1] + (width-stores[i][1]))
        elif stores[i][0] == 2:
            total += (height-now[1]) + (width-stores[i][1])
        else:
            total += width + min(now[1]+stores[i][1], height-now[1] + height-stores[i][1])

print(total)

