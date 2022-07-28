# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            tmp = []
            cnt = 0
            while cnt < 6:
                num = random.randrange(1,46)
                if num not in tmp:
                    tmp.append(num)
                    cnt += 1    
            tmp.sort()
            self.number_lines.append(tmp)
        #print(self.number_lines)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        date = Lotto.get_draw_date(draw_number)
        asc = 65
        print("=======================================================")
        print("제 {} 회 로또".format(draw_number))
        print("=======================================================")
        print("추첨일 : {}/{}/{} (토)".format(date[0], date[1], date[2]))
        print("=======================================================")
        for i in range(len(self.number_lines)):
            print("{} : {}".format(chr(asc+i), self.number_lines[i]))


    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        tmp = Lotto.get_lotto_numbers(draw_number)
        main_numbers = tmp[0]
        bonus_number = tmp[1]
        asc = 65

        print("=======================================================")
        print("당첨 번호 : {} + {}".format(main_numbers, bonus_number))
        print("=======================================================")

        for i in range(len(self.number_lines)):
            tmp2 = Lotto.get_same_info(main_numbers, bonus_number, self.number_lines[i])
            same_main_counts = tmp2[0]
            is_bonus = tmp2[1]
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            if is_bonus:
                if ranking < 0:
                    print("{} : {}개 + 보너스 일치 (낙첨)".format(chr(asc+i), same_main_counts))
                else:
                    print("{} : {}개 + 보너스 일치 ({}등 당첨!)".format(chr(asc+i), same_main_counts, ranking))
            else:
                if ranking < 0:
                    print("{} : {}개 일치 (낙첨)".format(chr(asc+i), same_main_counts))
                else:
                    print("{} : {}개 일치 ({}등 당첨!)".format(chr(asc+i), same_main_counts, ranking))

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        number_json = open('data/lotto_{}.json'.format(draw_number), encoding= 'utf-8')
        date_json = json.load(number_json)
        date = tuple(date_json["drwNoDate"].split('-'))

        return date
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        number_json = open('data/lotto_{}.json'.format(draw_number), encoding= 'utf-8')
        lotto_json = json.load(number_json)
        main = []
        for key,value in lotto_json.items():
            if key.startswith('drwt'):
                main.append(value)
        bonus = lotto_json['bnusNo']
        main.sort()
        
        return (main, bonus) 
        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
        for i in line:
            if i in main_numbers:
                same_main_counts += 1
        
        if bonus_number in line:
            is_bonus = True
        
        return (same_main_counts, is_bonus)
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
            return 1
        elif same_main_counts == 5 and is_bonus == True:
            return 2
        elif same_main_counts == 5:
            return 3
        elif same_main_counts == 4:
            return 4
        elif same_main_counts == 3:
            return 5
        else:
            return -1
        # return ranking
