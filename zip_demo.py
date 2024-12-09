import numpy as np 

x=[[1,2,3],
[4,5,6],
[7,8,9]]

y=[2.5,3.5,4.5]

for nx,my in zip(x,y):
    print('x = ',nx,': y = ',my)

