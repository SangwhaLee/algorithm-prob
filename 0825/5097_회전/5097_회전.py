import sys

sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    # arr 리스트의 가장 앞에 값을 바로 arr 맨뒤에 다시 넣어주면 된다
    for _ in range(M):
        arr.append(arr.pop(0))

    print("#{} {}".format(tc, arr[0]))
