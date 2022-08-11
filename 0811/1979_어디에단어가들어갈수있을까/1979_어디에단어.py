import sys

sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(T):
    #총 규격의 사이즈 N, 단어의 길이 K
    N, K = map(int, input().split())

    #현재 칸 상태에 대한 정보 입력
    arr = [list(map(int,input().split())) for _ in range(N)]

    #총 개수
    total = 0

    #가로 단어칸 부터 확인
    for i in range(N):
        #단어의 사이즈는 정해져 있으므로 확인할 칸이 줄어든다
        for j in range(N-K+1):
            #단어의 시작점은 벽에 붙어있는 상태에서 시작된다.
            if arr[i][j] == 1 and (j == 0 or arr[i][j-1] == 0):
                space = 0
                #시작점에서 부터 K만큼 arr의 값을 더한다
                #더한 값이 K와 같으면 단어가 들어갈 수 있는 칸이 된다.
                for k in range(j, j+K):
                    space += arr[i][k]
                    #print(space)
                    if space == K and (k == N-1 or arr[i][k+1] == 0):
                        total += 1

    for i in range(N):
        for j in range(N-K+1):
            if arr[j][i] == 1 and (j == 0 or arr[j-1][i] == 0):
                space = 0
                for k in range(j, j+K):
                    space += arr[k][i]
                    if space == K and (k == N-1 or arr[k+1][i] == 0):
                        total += 1

    print("#{} {}".format(tc+1,total))


    #print("#{} {}".format(tc+1, total))
