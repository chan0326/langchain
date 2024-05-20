import os
import sys

from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example.crime_model import crimeModel
from example.crime_util import Reader
import pandas as pd

class CrimeService:

    def __init__(self):
        self.data = crimeModel()
        this = self.data
        this.dname = 'C:\\Users\\AIA\\python\\vienna-chat-server\\get_sample\\example\\data\\'
        this.sname = 'C:\\Users\\AIA\\python\\vienna-chat-server\\get_sample\\example\\save\\'
        this.cctv_in_seoul = 'cctv_in_seoul.csv'
        this.crime_in_seoul = 'crime_in_seoul.csv'
        self.crime_rate_columns = ['살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']
        self.crime_columns = ['살인','강도','강간','절도','폭력']
        self.arrest_columns = ['살인검거','강도검거','강간검거','절도검거','폭력검거']



    def cctv_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}{self.data.cctv_in_seoul}', encoding='utf-8', thousands=',')
    
    def crime_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}{self.data.crime_in_seoul}')
    
    def save_model(self, fname: str, dframe: pd.DataFrame) -> pd.DataFrame:
        return dframe.to_csv(f'{self.data.sname}{fname}', sep=',', na_rep='NaN')
    
    def save_police_position(self, fname: str, dframe: pd.DataFrame) -> None:
        station_names = []
        for name in dframe['관서명']:  
            station_names.append('서울' + str(name[:-1]) + '경찰서') 
        station_addrs = []
        station_lats = [] # 위도
        station_lngs = [] # 경도
        reader = Reader()
        gmaps = reader.gmaps() 
        for name in station_names:
            tmp = gmaps.geocode(name, language='ko')
            station_addrs.append(tmp[0].get("formatted_address"))
            tmp_loc = tmp[0].get("geometry")
            station_lats.append(tmp_loc['location']['lat'])
            station_lngs.append(tmp_loc['location']['lng'])
        
        gu_names = []
        for name in station_addrs:
            tmp = name.split()
            tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(tmp_gu)
        
        dframe['구별'] = gu_names
        #구 와 경찰서의 위치가 다른 경우
        dframe.loc[dframe['관서명'] == '혜화서', ['구별']] = '종로구'
        dframe.loc[dframe['관서명'] == '서부서', ['구별']] = '은평구'
        dframe.loc[dframe['관서명'] == '강서서', ['구별']] = '양천구'
        dframe.loc[dframe['관서명'] == '종암서', ['구별']] = '성북구'
        dframe.loc[dframe['관서명'] == '방배서', ['구별']] = '서초구'
        dframe.loc[dframe['관서명'] == '수서서', ['구별']] = '강남구'
        self.save_model(fname, dframe)
        print(dframe)
        return dframe
    


            

            
    
    
    
if __name__ == '__main__':
    crime = CrimeService()
    # crime.save_model('test_cctv.csv', crime.cctv_dataframe())
    # crime.save_model('test_crime.csv', crime.crime_dataframe())
    crime.save_police_position('test_police.csv', crime.crime_dataframe())
    print(crime.cctv_dataframe())
    print(crime.crime_dataframe())
    print('파일 저장 완료')
