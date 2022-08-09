import sys

sys.stdin = open('sample_input.txt', 'r')

N = int(input())

for i in range(N):
    distance, total, c_num = map(int, input().split())
    c_station = list(map(int,input().split()))
    bp = False

#0이 나오는 경우를 미리 알아내기 위한 부분
#충전소 리스트의 사이의 값이 K보다 크면 0출력
    start = 0
    for j in c_station: # 1 3 5 7
        if j-start > distance:
            print('#{} 0'.format(i+1))
#여기서 바로 break,continue는 효과가 없기 때문에
#해당 반복문 밖에서 사용하기 위한 값
            bp = True
            break
        else:
            start = j

#0이 출력되는 조건이면 해당 TC 전체를 스킵
    if bp:
        continue    

    now = 0
    cnt = 0
#현재 위치가 종점의 위치보다 커지면 종료
    while now < total:
        now += distance
#종점에 도달하면 있을 무한 루프를 대비한 방지책
        if now >= total:
            break
#최대거리 전진한 위치부터 역으로 한칸씩 후진
        for k in range(now,-1,-1):
            # print(k) 
            if k in c_station:
                now = k
                cnt += 1
                break
    
    print("#{} {}".format(i+1, cnt))