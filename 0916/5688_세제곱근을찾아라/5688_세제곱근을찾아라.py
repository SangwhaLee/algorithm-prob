import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    N = int(input())
    step = 1
    while step**3 < N:
        step += 1

    if step**3 > N:
        print("#{} {}".format(tc,-1))
    else:
        print("#{} {}".format(tc, step))