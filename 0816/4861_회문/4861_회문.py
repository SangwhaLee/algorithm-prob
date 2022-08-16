import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    # 받은 문자열을 2차원 리스트로 만들어서 저장
    letters = [list(input()) for _ in range(N)]

    # 2차원 리스트내의 모든 값을 순회하며 회문이 있는지 확인
    for i in range(N):
        # M크기의 단어를 확인해야 하므로 길이를 제한
        for j in range(N-M+1):
            # 회문 여부를 확인하기 위한 변수
            flag = True
            # 회문 확인의 시작점
            left = j
            # 회문 확인의 끝점
            right = j+M-1
            # 회문이라면 시작점의 값과 끝점의 값이 계속같아야 한다.
            # 회문의 길이가 홀수이건 짝수이건 상관이 없다
            while left < right:
                if letters[i][left] != letters[i][right]:
                    flag = False
                    break
                left += 1
                right -= 1
            # 만약 끝까지 회문이 부정되지 않는다면 그건 회문이라는 뜻이다
            if flag:
                print("#{}".format(tc),end=' ')
                for k in range(j, j+M):
                    print(letters[i][k],end='')
                print()

            # 같은 방법으로 세로축도 확인해주면 된다
            flag = True
            left = j
            right = j + M - 1
            while left < right:
                if letters[left][i] != letters[right][i]:
                    flag = False
                    break
                left += 1
                right -= 1
            if flag:
                print("#{}".format(tc), end=' ')
                for k in range(j, j + M):
                    print(letters[k][i], end='')
                print()