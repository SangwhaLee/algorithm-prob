import sys
N, K = map(int, sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))

now = 0

# 첫 연속된 K일 만큼 온도 합
for i in range(K):
    now += numbers[i]
# 최대 온도를 저장할 변수
maxV = now

# 전날과 오늘의 온도합은 K-1일 만치의 온도가 겹치게 된다
# 전날 온도의 합에서 첫날의 값을 빼고 오늘 온도의 합의 마지막날의 값을 넣어주면 된다
for i in range(1,N-K+1):
    now = (now - numbers[i-1] + numbers[i+K-1])
    if now > maxV:
        maxV = now

print(maxV)