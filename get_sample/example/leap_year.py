from example.utils import myRandom


class LeapYear:

    def __init__(self) -> None:
        print(f'utils.py myRandom() 를 이용하여 윤년계산기 객체를 생성합니다')
        print ('(ex) 2020년은 윤년입니다. 단 컴프리헨션을 사용합니다')
        

    def is_leap(self):
        year = myRandom(2000,2024)
        y='윤년' if (year %4 ==0 and year %100 !=0) or year % 400 == 0  else '평년'
        print(f'{year}년은 {y}입니다')
        return year