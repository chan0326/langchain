class Contract:

    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone
        
    @staticmethod
    def add_member():
            name = input('이름 입력: ').title()
            if name in members.keys(): 
               print('이미 존재하는 이름입니다.')
            else :
                phone = input('전화번호 입력: ')
                print('----------')
                print(f'*****{name} 입력 완료*****')
                print(f'{name}:', phone)
                print('----------')
                members[name] = phone
    @staticmethod
    def search_member():
            name = input('검색할 이름 입력: ').title()
            phone = members.get(name, '존재하지 않습니다.')
            print('----------')
            print(f'{name}:', phone)
            print('----------')
    
    @staticmethod
    def update_member():
        name = input('수정할 이름 입력: ').title()
        if name not in members.keys(): # members.keys(): key만 추출하기
            print('----------')
            print(f'{name} 회원은 존재하지 않습니다.')
            print('----------')
            pass # loop 계속 진행
        else:
            phone = input('새로운 전화번호 입력: ')
            members[name] = phone
            print('----------')
            print(f"*****{name} 수정 완료*****")
            print(f'{name}:', phone)
            print('----------')
    
    @staticmethod
    def delete_member():
        name = input('삭제할 이름 입력: ').title()
        if name not in members.keys():
                print('----------')
                print(f'{name} 회원은 존재하지 않습니다.')
                print('----------')
                pass
        else:
                ask = input(f"{name} 회원을 정말로 삭제할까요?(y): ").lower()
                if ask == 'y':
                    del members[name]
                    print('----------')
                    print(f"*****{name} 삭제 완료*****")
                    print('----------')
                else:
                    print('----------')
                    print(f'{name} 회원을 삭제하지 않았습니다.')
                    print('----------')
                    pass
    
    @staticmethod
    def list_member():
        print('----------')
        for k, v in members.items(): # members.items(): key, value 추출하기
            print(f'{k}: {v}')
        print('----------')

            


if __name__ == "__main__":

    members = {}
    while True:
        menu = input('회원정보 추가(a), 검색(f), 수정(u), 삭제(d), 목록(s), 종료(x): ')
        if menu=='a':
            Contract.add_member()


        elif menu=='f':
            Contract.search_member()
            


        elif menu=='u':
            Contract.update_member()


        elif menu=='d':
            Contract.delete_member()


        elif menu=='s':
            Contract.list_member()


        elif menu=='x':
            print('----------')
            print('프로그램을 종료합니다.')
            print('----------')
            break # loop 끝내기