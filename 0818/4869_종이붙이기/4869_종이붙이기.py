import sys
sys.stdin = open('sample_input.txt','r')

'''
이 문제는 풀때 손으로 경우의 수를 확인하느라 오래 걸릴 수 밖에 없었다.
문제에서 주어진 힌트로는
10 - 1
20 - 3
30 - 5
40 - ?
50 - 21
60 - ?
70 - 85
이 중에서 N이 40일 때의 경우는 직접 구할 수 있을거 같아 손으로 그리면 구했고 그 결과 11이라는 0값을 확인했다.
그려진 종이의 경우의 수를 N/10이 홀수인 경우엔 전의 모양에서 가로길이 10짜리 종이를 하나씩 더한 정도의 변화밖에 없었다.
반면 N/10이 짝수인 경우 10짜리 종이를 두개 붙여놓은 경우나 20짜리 종이를 활용할 수 있게 되어 새롭게 추가되는 것이 더 많았다.
이를 확인하고 숫자간의 패턴이 있을것이라 판단해 알아낸것이 K = (M-1)*2 + 1 or 3 이 되는 식이었다.
여기서 M은 K보다 10 작은 값에서 발생한 경우의 수이다.
'''

# 입력 받는 N의 값은 300이 최대이기 때문에 그에 맞춰 메모이제이션 리스트를 선언
numbers = [0]*31
# N이 10인 경우는 1가지 뿐이다
numbers[1] = 1

# 종이붙이기 경우의 수를 구하는 함수
def paper(N):
    # 메모이제이션 리스트안에 있을 경우 반환
    if numbers[N//10] != 0:
        return numbers[N//10]
    # 현재 N/10의 값이 홀수인 경우와 짝수인 경우가 달라진다
    else:
        if (N//10) % 2:
            numbers[N//10] = (paper(N-10)-1)*2 + 1
        else:
            numbers[N // 10] = (paper(N - 10) - 1) * 2 + 3
        return numbers[N // 10]

paper(300)

for tc in range(1,int(input())+1):
    N = int(input())

    print("#{} {}".format(tc, numbers[N//10]))
