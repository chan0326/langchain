from example.utils import Member


class BMI():
    def __init__(self) -> None:
        '''utils.py / Members(), myRandom() 를 이용하여 BMI 지수를 구하는 계산기를 작성합니다.'''

    def getbmi (self, weight, height):
        '''BMI 지수를 구하는 함수입니다.'''
        this = Member()
        this.weight = weight
        this.height = height
        this.name = '홍길동'
        bmi = this.weight / (this.height/100)**2
        
        if bmi < 18.5: return f'{this.name}님은 저체중입니다.'
        elif 18.5 <= bmi < 23: return f'{this.name}님은 정상입니다.'
        elif 23 <= bmi < 25: return f'{this.name}님은 과체중입니다.'
        elif 25 <= bmi < 30: return f'{this.name}님은 비만입니다.'
        else: return f'{this.name}님은 고도비만입니다.'

        