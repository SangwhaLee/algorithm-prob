from collections import deque

N, k = map(int, input().split())

belt = list(map(int,input().split()))
robot = [0]*len(belt)
lastest_idx = -1

while True:
    # 1. 회전: belt의 각 구성요소를 다음 인덱스로 이동 마지막 인덱스에 있는 값은 첫 인덱스로 이동, 이동 후에 내리는 칸에 있는 로봇은 내려야 한다
    # 2. 가장 뒤쪽에 있는 로봇의 다음 인덱스가 비어있으면서 내구도는 존재할 때 이동, 로봇이 이동 후에 내리는 칸에 있는 로봇은 내려야 한다
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올린다
    # 4. 위 모든 과정 중에 내구도가 0인 칸의 개수가 k개 이상이면 과정을 종료하고 그때가 몇단계 였는지 출력

    last_belt =

