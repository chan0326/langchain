import random



# class RPS:

#     def __init__(self) -> None:
#         print(f'utils.py myRandom() 를 이용하여 가위바위보 객체를 생성합니다')
    
#     def play(self):
#         rps = ['가위', '바위', '보']
#         player = myRandom(0,3)
#         com = myRandom(0,3)
#         print(f'플레이어 : {rps[player]} vs 컴퓨터 : {rps[com]}')
#         if player == com: print('비겼습니다')
#         elif (player == 0 and com == 1) or (player == 1 and com == 2) or (player == 2 and com == 0): print('컴퓨터 승리')
#         else: print('플레이어 승리')

def myRandom(start, end): return random.randint(start, end-1)

if __name__ == '__main__':
    rps = ['가위', '바위', '보']
    player = input('가위(0), 바위(1), 보(2) 중 하나를 입력하세요 : ')
    com = myRandom(0,3)
    print(f'플레이어 : {rps[int(player)]} vs 컴퓨터 : {rps[com]}')
    if player == com: print('비겼습니다')
    elif (player == 0 and com == 1) or (player == 1 and com == 2) or (player == 2 and com == 0): print('컴퓨터 승리')
    else: print('플레이어 승리')
1