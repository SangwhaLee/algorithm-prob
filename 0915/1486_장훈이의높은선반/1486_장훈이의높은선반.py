import sys
sys.stdin = open('input.txt','r')

# 직원들의 키의 합은 순서를 생각할 필요 없기 때문에 조합을 활용한다.
# members는 탑을 이루는 직원들을 모은 리스트, idx는 마지막으로 추가된 직원의 다음 리스트 상 인덱스 번호이다
def combination(members, idx):
    # 탑의 높이가 선반 이상이 될 경우 tower 리스트의 그 높이를 추가한다
    global tower
    if sum(members) >= B:
        tower.append(sum(members))
        return
    # 탑의 높이가 아직 선반 이상이 아닌 경우 새로운 멤버를 추가한다
    # 순열이 아닌 조합이기 때문에 이미 한 번 추가한 사람은 신경 쓸 필요가 없으므로 idx를 통해 마지막으로 추가 된 사람까지는 무시한다.
    for i in range(idx,N):
        # visited를 사용하지 않을 경우 모든 경우의 수를 확인할 수 없게 된다.
        if not visited[i]:
            visited[i] = True
            members.append(heights[i])
            combination(members, i+1)
            visited[i] = False
            members.pop()

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    heights = list(map(int,input().split()))
    visited = [False]*N
    tower = []

    combination([], 0)

    print("#{} {}".format(tc,min(tower)-B))
