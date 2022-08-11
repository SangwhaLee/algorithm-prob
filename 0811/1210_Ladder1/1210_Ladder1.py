import sys

sys.stdin = open('input.txt','r')

def ladder_game(arr, i, j):
    while i < 99: #사다리가 맨밑에 도달하면 반복문 그만
        #print("i:{} j:{} ".format(i, j))
        if j < 99 and arr[i][j+1] == 1: #우측벽에 붙어있을땐 해당 되지 않음
            while j < 99 and arr[i][j+1] == 1: #위와 동일한 조건
                j += 1 #옆길이 나타나면 오른쪽으로 이동할 수 있을만큼 이동
            i += 1 #옆길 다 통과하고 난 뒤에는 한칸 아래로 전진 무한루프 방지
        elif j > 0 and arr[i][j-1] == 1:
            while j > 0 and arr[i][j-1] == 1:
                j -= 1
            i += 1
        else:
            i += 1

    return i, j


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    for i in range(100): #사다리 게임 시작하는 점을 확인 (1을 찾는다)
        if arr[0][i] == 1: #1을 찾은 경우
            tmp = ladder_game(arr, 0, i) #좌표랑 함께 입력
            if arr[tmp[0]][tmp[1]] == 2:
                print("#{} {}".format(tc, i))
                break