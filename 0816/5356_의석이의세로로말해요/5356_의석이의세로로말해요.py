import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    # 입력받을 수있는 최대 크기의 판을 만들어 정수 0으로 채운다
    board = [[0]*15 for _ in range(5)]
    # 입력 받는 리스트
    letters = [list(input()) for _ in range(5)]
    # 세로로 읽은 단어
    word = ''

    for i in range(5):
        length = 0
        # len() 내장함수를 대체하기 위한 반복문
        for j in letters[i]:
            length += 1
        # 위에서 구한 길이를 통해 미리 만들어논 판에 입력받은 값을 하나하나 저장한다
        for j in range(length):
            board[i][j] = letters[i][j]

    # 최대크기 판의 내부를 순회하며 정수 0이 아닌것만을 word에 더한다
    for i in range(15):
        for j in range(5):
            if board[j][i] == 0:
                continue
            word += board[j][i]

    print("#{} {}".format(tc,word))