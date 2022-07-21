import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    right_num = False;
    while not right_num:
        N = int(input('1이상 10000이하의 숫자를 입력하세요.: '))
        if N < 1 or N > 10000:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
        else:
            if N > answer:
                print('Up!!!\n')
                counts += 1
                continue
            elif N < answer:
                print('Down!!!\n')
                counts += 1
                continue
            else:
                print(f'Correct!!! {counts}만에 정답을 맞히셨습니다.\n')
            
            choice = input('게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요. : ')
            if choice == 'y':
                break
            elif choice == 'n':
                print('이용해주셔서 감사합니다. 게임을 종료합니다.\n')
                is_playing = False
                break
            else:
                print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.\n')
                is_playing = False
                break

            