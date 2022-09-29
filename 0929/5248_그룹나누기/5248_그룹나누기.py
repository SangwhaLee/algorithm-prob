import sys
sys.stdin = open('sample_input.txt','r')

def find_set(x):
    if x == students[x]:
        return x
    else:
        return find_set(students[x])


def union(x, y):
    students[find_set(y)] = find_set(x)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    vote = list(map(int,input().split()))
    students = [0]*(N+1)
    for i in range(1,N+1):
        students[i] = i

    for i in range(0,M*2,2):
        union(vote[i], vote[i+1])

    cnt_set = set()
    for i in range(1,N+1):
        cnt_set.add(find_set(students[i]))

    print(students)
    print("#{} {}".format(tc, len(cnt_set)))