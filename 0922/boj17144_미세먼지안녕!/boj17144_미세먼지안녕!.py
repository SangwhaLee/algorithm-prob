import copy

def dust_diffusion():
    global room
    diffused_room = copy.deepcopy(room)

    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                cnt = 0
                for k in range(4):
                    ni = di[k] + i
                    nj = dj[k] + j
                    if ni < 0 or ni >= R or nj < 0 or nj >= C:
                        continue
                    if room[ni][nj] != -1:
                        cnt += 1
                        diffused_room[ni][nj] += room[i][j]//5
                diffused_room[i][j] -= (room[i][j]//5)*cnt
    room = diffused_room

# 공기청정기의 각 영역의 가장 뒤쪽에서부터 시작해 바람의 흐름과 반대방향으로 각 미세먼지가 이동한다
def fresher_on():
    global room
    # 공기청정기 기준 위쪽에 있는 영역부터 해결
    st = (fresher[0],0)
    step = 2*C + 2*(st[0]) - 3
    now = [st[0]-1, st[1]]
    while step > 0:
        if now[0] == 0 and now[1] == 0:
            room[now[0]][now[1]] = room[now[0]][now[1]+1]
            now[1] += 1
        elif now[0] == st[0] and now[1] == st[1]+1:
            room[now[0]][now[1]] = 0
            now[1] -= 1
        elif now[0] == 0 and now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]+1][now[1]]
            now[0] += 1
        elif now[0] == st[0] and now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]][now[1]-1]
            now[1] -= 1
        elif now[1] == 0:
            room[now[0]][now[1]] = room[now[0]-1][now[1]]
            now[0] -= 1
        elif now[0] == 0:
            room[now[0]][now[1]] = room[now[0]][now[1]+1]
            now[1] += 1
        elif now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]+1][now[1]]
            now[0] += 1
        elif now[0] == st[0]:
            room[now[0]][now[1]] = room[now[0]][now[1] -1]
            now[1] -= 1
        step -= 1

    # 공기 청정기 아래쪽의 영역을 해결
    st = (fresher[1], 0)
    step = 2*C + 2*(R-st[0]-1) - 3
    now = [st[0]+1, st[1]]
    while step > 0:
        if now[0] == R-1 and now[1] == 0:
            room[now[0]][now[1]] = room[now[0]][now[1]+1]
            now[1] += 1
        elif now[0] == st[0] and now[1] == st[1]+1:
            room[now[0]][now[1]] = 0
            now[1] -= 1
        elif now[0] == R-1 and now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]-1][now[1]]
            now[0] -= 1
        elif now[0] == st[0] and now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]][now[1]-1]
            now[1] -= 1
        elif now[1] == 0:
            room[now[0]][now[1]] = room[now[0]+1][now[1]]
            now[0] += 1
        elif now[0] == R-1:
            room[now[0]][now[1]] = room[now[0]][now[1]+1]
            now[1] += 1
        elif now[1] == C-1:
            room[now[0]][now[1]] = room[now[0]-1][now[1]]
            now[0] -= 1
        elif now[0] == st[0]:
            room[now[0]][now[1]] = room[now[0]][now[1]-1]
            now[1] -= 1
        step -= 1


R, C, T = map(int,input().split())
room = list(list(map(int,input().split())) for _ in range(R))
fresher = []
for i in range(R):
    if room[i][0] == -1:
        fresher.append(i)
        fresher.append(i+1)
        break

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while T > 0:
    dust_diffusion()
    fresher_on()
    T -= 1

total = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            total += room[i][j]

# print(room)
print(total)