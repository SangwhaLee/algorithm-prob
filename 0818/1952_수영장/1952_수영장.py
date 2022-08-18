import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    d, m, m3, y= map(int, input().split())
    plan = list(map(int,input().split()))

