import sys
sys.stdin = open('sample_input.txt','r')


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = []
    right = []
    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    global answer2
    ll = len(left)
    rl = len(right)
    result = [0]*(ll+rl)
    li, ri = 0, 0
    i = 0
    if left[-1] > right[-1]:
        answer2 += 1
    while li < ll or ri < rl:
        if li < ll and ri < rl:
            if left[li] <= right[ri]:
                result[i] = left[li]
                i += 1
                li += 1
            else:
                result[i] = right[ri]
                i += 1
                ri += 1
        elif ri < rl:
            result[i] = right[ri]
            i += 1
            ri += 1
        elif li < ll:
            result[i] = left[li]
            i += 1
            li += 1

    return result


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    answer2 = 0
    arr = merge_sort(arr)

    print("#{} {} {}".format(tc, arr[N//2], answer2))

