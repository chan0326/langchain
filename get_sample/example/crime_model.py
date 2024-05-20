
from dataclasses import dataclass
import pandas as pd


@dataclass
class crimeModel:
    _dname : str = '' # data name
    _sname : str = '' # save name
    _fname : str = '' # file name
    _cctv_in_seoul : str = ''
    _crime_in_seoul : str = ''

   
    @property
    def dname(self) -> str : return self._dname
    @dname.setter
    def dname(self, dname: str) : self._dname = dname
    @property
    def sname(self) -> str: return self._sname
    @sname.setter
    def sname(self, sname: str): self._sname = sname
    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname: str): self._fname = fname

    @property
    def cctv_in_seoul(self) -> str: return self._cctv_in_seoul
    
    @cctv_in_seoul.setter
    def cctv_in_seoul(self, cctv_in_seoul: pd.DataFrame): self._cctv_in_seoul = cctv_in_seoul

    @property
    def crime_in_seoul(self) -> str: return self._crime_in_seoul

    @crime_in_seoul.setter
    def crime_in_seoul(self, crime_in_seoul: pd.DataFrame): self._crime_in_seoul = crime_in_seoul





