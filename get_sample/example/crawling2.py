import csv
from urllib.request import urlopen

from bs4 import BeautifulSoup
class ScrapBugs: # 파이썬 크롤링 하는 방법

    

    def scrap(self):
        print('벅스 실시간 차트')
        url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
        html_doc = urlopen(url) # url을 열어서 html_doc에 저장
        soup = BeautifulSoup(html_doc, 'lxml') # html_doc을 lxml로 파싱
        list1 = self.find_music(soup, 'title') 
        list2 = self.find_music(soup, 'artist')

        # 순위와 함께 출력
        ranked_list = list(enumerate(zip(list1, list2), start=1))
        for rank, (title, artist) in ranked_list:
            print(f"{rank}. {title} - {artist}")
            print(ranked_list)
        save_path = 'C:/Users/AIA/python/vienna-chat-server/get_sample/example/data/bugs_chart.csv'
        self.save_to_csv(ranked_list, save_path) # csv 파일로 저장

        # 데이터를 여러가지 방법으로 출력
        a = [i if i ==0  or i ==0 else i for i in range(1)]
        b = [i if i ==0  or i ==0 else i for i in []]
        c = [(i, j)for i, j in enumerate([])]
        d = {i:j for i, j in zip(list1, list2)}
        e = {i + j for i, j in zip(list1, list2)}
        l2 = list(zip(list1, list2))
        d1 = dict(zip(list1, list2)) 
        # print(d1)
        return d
    
    def find_music(self , soup : BeautifulSoup, class_name : str):
        list = soup.find_all('p', {'class': class_name}) # p 태그의 class 이름이 title인 것을 찾아서 list에 저장
        return [i.get_text().strip().replace('\n', '').replace('\r', '') for i in list]
        # return [i.get_text() for i in list] 위에 코드와 같은 의미이다. strip()은 공백을 제거하는 함수이다.

    def save_to_csv(self, ranked_list, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Rank', 'Title', 'Artist'])  # 헤더 작성
            for rank, (title, artist) in ranked_list:
                writer.writerow([rank, title, artist])  # 데이터 작성
if __name__ == '__main__':
    bugs = ScrapBugs()
    bugs.scrap()
    

    



        


