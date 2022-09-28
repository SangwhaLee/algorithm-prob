import sys
sys.stdin = open('sample_input.txt','r')

def quicksort(l, r):
    if l < r:
        s = partition(l, r)
        quicksort(l, s-1)
        quicksort(s+1, r)


def partition(l,r):
    pivot = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quicksort(0,len(arr)-1)
    print("#{} {}".format(tc, arr[N//2]))