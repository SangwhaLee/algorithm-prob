import sys

sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    # 목표 단어의 각 글자와 그 수를 저장할 딕셔너리
    count = dict()
    # 목표 단어 , 타겟
    target = input()
    # 글자목록
    letters = input()

    # 타겟의 각 글자를 딕셔너리의 key로 두고 value는 정수 0으로 저장
    for i in target:
        if i not in count.keys():
            count[i] = 0

    # 만약 글자목록의 글자가 딕셔너리의 키값으로 존재한다면 딕셔너리의 해당 키의 value 값을 하나 증가
    for i in letters:
        if i in count.keys():
            count[i] += 1

    maxV = 0

    # 딕셔너리의 value를 순회하며 가장 큰 값을 결정
    for v in count.values():
        if v > maxV:
            maxV = v

    print("#{} {}".format(tc, maxV))