import sys
sys.stdin = open('sample_input.txt','r')

# depth는 몇월인지를 나타내기 위한 변수, 여태까지의 총합을 저장하는 total
def swimming(depth, total):
    global minimum
    # 만약 1년 전부를 확인했으면 기존의 최소값과 비교
    if depth == 12:
        minimum = min(total, minimum)
        return

    #만약 해당 월에 수영장 사용이 없거나 혹은 이미 사용등록이 완료된 월이면 그냥 스킵
    if schedule[depth] == 0 or visited[depth]:
        swimming(depth+1, total)
        return

    # 완전탐색을 통해 네 가지의 지불 방법을 전부 한 번씩 적용하여 확인해본다 3개월이나 1년은 한 번 적용하면 그 이후의 월에도 사용등록을 해준다
    for i in range(4):
        if i == 0:
            visited[depth] = True
            swimming(depth+1, total + (prices[i]*schedule[depth]))
            visited[depth] = False
        elif i == 1:
            visited[depth] = True
            swimming(depth + 1, total + prices[i])
            visited[depth] = False
        elif i == 2:
            if depth <= 9:
                visited[depth], visited[depth+1], visited[depth+2] = True, True, True
                swimming(depth + 1, total + prices[i])
                visited[depth], visited[depth + 1], visited[depth + 2] = False, False, False
            else:
                for j in range(12-depth):
                    visited[depth+j] = True
                swimming(depth+1, total + prices[i])
                for j in range(12-depth):
                    visited[depth+j] = False
        else:
            if depth == 0:
                for j in range(12):
                    visited[depth+j] = True
                swimming(depth + 1, total + prices[i])
                for j in range(12):
                    visited[depth+j] = False
            else:
                for j in range(12-depth):
                    visited[depth+j] = True
                swimming(depth+1, total + prices[i])
                for j in range(12-depth):
                    visited[depth+j] = False


for tc in range(1, int(input())+1):
    prices = list(map(int, input().split()))
    schedule = list(map(int,input().split()))
    # 사용등록이 되어있는 달인지 알기 위한 리스트
    visited = [False]*12
    minimum = 1e9
    swimming(0, 0)
    print("#{} {}".format(tc, minimum))
