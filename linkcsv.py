import requests as reqq
import pandas as pd
from io import StringIO
url="https://github.com/vinodbabusir/IPL2022/blob/main/IPL_2022_21042023.csv"
header={'User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req= reqq.get(url,headers=header)
data=StringIO(req.text)
frame=pd.read_csv(data)
print(frame)