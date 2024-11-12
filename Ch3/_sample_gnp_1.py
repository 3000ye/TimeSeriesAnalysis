import pandas as pd

# 读取数据文件
da = pd.read_csv("../ftsdata/q-gnp4710.txt", sep='\s+', dtype=float)
data = pd.DataFrame(da["VALUE"].values, index=pd.date_range(start="1947-01", periods=len(da), freq='QE'), columns=["value"])
data.head()