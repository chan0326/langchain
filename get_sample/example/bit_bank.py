import datetime
import utils
today = datetime.datetime.now()

class Account:

    def __init__(self, name, account_number, money) -> None:
        '''
        [요구사항(RFP)]
        은행이름은 비트은행이다.
        입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
        계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
        예를들면 123-12-123456 이다.
        금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
        '''
        self.BANK_NAME = '비트은행'
        self.name = name
        self.account_number = account_number
        self.money =  int(money)

    def __str__(self):
        return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")} ' \
               f'은행 : {self.BANK_NAME}, ' \
               f'입금자: {self.name},' \
               f'계좌번호: {self.account_number},' \
               f'금액: {self.money} 만원'
    # __str__의 목적은 문자열화를 하여 서로 다른 객체 간의 정보를 전달하는 데 사용한다.
    
    def __repr__(self):
        return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")} ' \
               f'은행 : {self.BANK_NAME}, ' \
               f'입금자: {self.name},' \
               f'계좌번호: {self.account_number},' \
               f'금액: {self.money} 만원' 
    # __repr__의 목적은 객체를 문자열화하여 객체 자체를 표현하는 데 사용한다.


    @staticmethod 
    def creat_account_number():
            name = input('이름')
            account_number = f'{utils.myRandom(1000, 10000)}-{utils.myRandom(10, 100)}-{utils.myRandom(100000, 1000000)}'
            money = input('금액')
            this = Account(name=name, account_number=account_number, money=money)
            print(f'__str__ 출력')
            print(f'{this} ... 개설되었습니다.')
            print(f'__repr__ 출력')
            print(f'{this}... 개설되었습니다.')
            ls.append(this)

    @staticmethod
    def deposit (ls, account_number, money):
        for i in ls:
            if i.account_number == account_number:
                i.money += money
                print(f'{money}만큼 입금되었습니다. 잔액은 {i.money}만원입니다.')

    @staticmethod
    def withdraw (ls, account_number, money):
        for i in ls:
            if i.account_number == account_number:
                i.money -= money
                print(f'{money}만큼 출금되었습니다. 잔액은 {i.money}만원입니다.')




    @staticmethod
    def find_account(ls, account_number):
        for i in ls:
            if i.account_number == account_number:
                return i

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]
                print(f'{account_number} ... 삭제되었습니다.')


import random        


def myRandom(start, end): return random.randint(start, end-1)

if __name__ == "__main__":
    ls = []
    while 1 :
        menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지 6.계좌조회')
        if menu == '0':
            break
        if menu == '1':
            Account.creat_account_number()
        elif menu == '2':
            for i in ls:
                print(i)
            if not ls:
                print('계좌가 없습니다.')
        elif menu == '3':
            account_number = input('입금할 계좌번호')
            deposit = int(input('입금액'))
            for i, j in enumerate(ls): #
                if j.account_number == account_number:
                    pass
            Account.deposit(ls, account_number, deposit)
        elif menu == '4':
            account_number = input('출금할 계좌번호')
            money = input('출금액')
            for i in ls:
                if i.account_number == account_number:
                    pass
            Account.withdraw(ls, account_number, money)
            # 추가코드 완성
        elif menu == '5':
            Account.del_account(ls, input('탈퇴할 계좌번호'))
        elif menu == '6':
            print(Account.find_account(ls, input('검색할 계좌번호') ))
        else:
            print('Wrong Number.. Try Again')
            continue