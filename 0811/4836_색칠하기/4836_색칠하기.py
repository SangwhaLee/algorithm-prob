import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    red = []
    blue = []
    arr = [[0]*10 for i in range(10)] #확인용 리스트를 하나 만든다
    cnt = 0

    for i in range(N):
        i1,j1,i2,j2,C = map(int, input().split())
        tmp = [i1,j1,i2,j2] #입력받은 두 좌표는 리스트에 저장
        if C == 1: #색에 따라 저장해놓은 좌표 리스트를 빨간색, 파란색으로 분류
            red.append(tmp)
        else:
            blue.append(tmp)

    for r in red: #해당 리스트에는 빨간색 영역의 좌표만 포함
        for i in range(r[0], r[2]+1):
            for j in range(r[1], r[3]+1):
                arr[i][j] = 1

    for b in blue: #해당 리스트에는 파랑색 영역의 좌표만 포함
        for i in range(b[0], b[2]+1):
            for j in range(b[1], b[3]+1):
                if arr[i][j] == 1:
                    cnt += 1

    print("#{} {}".format(tc+1, cnt))