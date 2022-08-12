import sys

sys.stdin = open('GNS_test_input.txt', 'r', encoding='UTF8')

T = int(input())
#두 개의 딕셔너리를 만들어 서로서로 치환할 수 있도록 한다. 숫자값도 문자열로 하여 key값이 될 수 있도록 한다
alphaToNum = {"ZRO":'0', "ONE":'1', "TWO":'2', "THR":'3', "FOR":'4', "FIV":'5', "SIX":'6', "SVN":'7', "EGT":'8', "NIN":'9'}
numToAlpha = {'0':"ZRO", '1':"ONE", '2':"TWO", '3':"THR", '4':"FOR", '5':"FIV", '6':'SIX', '7':'SVN', '8':'EGT', '9':"NIN"}

#카운팅 정렬 방법을 이용하긴 했지만 약간 다르다
def count_sort(arr, N):
    count_arr = [0]*10
    new_str = ''
    for i in range(N):
        count_arr[int(arr[i])] += 1 #딕셔너리로 받은 문자열값을 카운팅 배열에 저장

    for i in range(10): #카운팅 배열의 값을 이용해 문자열 덧셈
        new_str += count_arr[i]*str(i)

    return new_str


for tc in range(1,T+1):
    test, strN = input().split()
    N = int(strN)
    arr = list(input().split())
    n_arr = []
    for i in range(N):
        n_arr.append(alphaToNum[arr[i]]) #외계 숫자를 정수로 치환

    n_arr = list(count_sort(n_arr, N)) #일반정수로 이뤄진 문자열 반환

    for i in range(N):
        n_arr[i] = numToAlpha[n_arr[i]] #일반정수에서 외계숫자로 치환

    print("#{}".format(tc), end=' ')
    for i in n_arr:
        print(i, end=' ')
    print()