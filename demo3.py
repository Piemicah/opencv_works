import  pandas as pd
import numpy as np

#df = pd.read_csv('daily_csv.csv')
#print(df)

data = np.random.random((4,4))
row = ['x1','x2','x3','x4']
col = ['Red','Green','Blue','White']
mydata = pd.DataFrame(data,row,col)
mydata.to_csv('data2.csv')
