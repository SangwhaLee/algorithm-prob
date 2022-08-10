import sys

sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(T):
    arr = list(map(int,input().split()))
    isZero = False

    for i in range(1<<10):
        total = 0
        cnt = 0
        subset = []
        for j in range(10): #입력받는 리스트 값의 개수는 10개
            #2^10 = 1024개의 부분집합이 나타난다.
            if i&(1<<j):  #j라고 하는 값의 위치에 존재하는 값이 해당 부분집합에 속하는지를 확인
                          #i를 이진수로 만들어서 하나하나 확인하는 것과 같은 결과를 반환 
                subset.append(arr[j]) #빈 리스트에 부분집합에 속하는 '실제값'을 저장
        for j in subset:
            total += j
            cnt += 1 
            #부분집합이 공집합인 경우 total은 무조건 0이 된다. 때문에 공집합의 경우를 제외하기 위해 필요
        if total == 0 and cnt != 0:
            isZero = True
            break
    
    if isZero:
        print("#{} 1".format(tc+1))
    else:
        print("#{} 0".format(tc+1))