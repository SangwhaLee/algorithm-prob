import sys

sys.stdin = open('input.txt','r')

for tc in range(1,11):
    maxV = 1
    n = int(input())
    letters = [list(input()) for _ in range(100)]

# 회문을 확인할 글자수의 길이를 100에서 부터 내림차순으로 정해준다
    # 내림차순인 이유는 반복을 조금이라도 줄이기 위해
    for length in range(100, 2, -1):
        for i in range(100):
            for j in range(100-length+1):
                flag = True
                left = j
                right = j+length-1

                while left < right:
                    if letters[i][left] != letters[i][right]:
                        flag = False
                        break
                    left += 1
                    right -= 1
                # 만약 끝까지 회문이 부정되지 않는다면 그건 회문이라는 뜻이다
                # 회문이라는 것이 확인 되면 모든 반복문을 탈출한다
                if flag:
                    maxV = length
                    break

                flag = True
                left = j
                right = j+length-1
                while left < right:
                    if letters[left][i] != letters[right][i]:
                        flag = False
                        break
                    left += 1
                    right -= 1
                if flag:
                    maxV = length
                    break
            # 길이가 정해졌다면 뒤에 나오는 값은 전부 현재의 길이보다 짧다 반복할 필요가 없다
            if flag:
                break
        if flag:
            break

    print("#{} {}".format(tc, maxV))
