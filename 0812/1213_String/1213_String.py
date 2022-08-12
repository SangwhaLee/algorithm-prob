import sys

sys.stdin = open('test_input.txt','r', encoding= 'UTF8')

for tc in range(1,11):
    n = int(input())
    target = input()
    arr = input()
    cnt = 0
    length = 0
    short_l = 0

    for i in arr: #len()을 쓸수 없으니 직접 구해야한다.
        length += 1

    for i in target:
        short_l += 1

    for i in range(length - short_l + 1): #검색하고자 하는 단어가 들어갈 공간은 냅둔다.
        flag = True
        if arr[i] == target[0]:
            for j in range(short_l):
                if arr[i+j] != target[j]:
                    flag = False
                    break

            if flag: #그냥 for else 구문을 쓰면 된다.
                cnt += 1

    print("#{} {}".format(n, cnt))