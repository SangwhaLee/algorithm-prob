import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    # 찾아야 할 단어를 입력받는다
    target = input()
    # 단어를 찾아야 할 글자목록을 입력받는다
    letters = input()
    # 글자목록의 길이를 위한 변수
    length = 0
    # 목표 단어의 길이를 위한 변수
    t_length = 0
    # 목표 단어의 길이를 구하기 위한 반복문
    for i in target:
        t_length += 1
    # 글자목록의 길이를 구하기 위한 반복문
    for i in letters:
        length += 1

    # 글자목록을 순회하며 단어를 찾는다
    for i in range(length):
        # 만약 해당 위치의 글자가 단어의 첫글자와 같다면 확인한다
        if target[0] == letters[i]:
            # 지금 위치에서 찾고자 하는 단어의 길이만큼 이어진 글자의 집합체가 타겟과 같은가
            if target == letters[i:i+t_length]:
                print("#{} 1".format(tc))
                break

    else:
        print("#{} 0".format(tc))

