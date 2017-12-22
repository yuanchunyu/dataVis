import numpy as np
import pandas as pd

file=open('fuel2.csv')
data =pd.read_csv(file,sep=',')
#print data["state"]
data["f"]=""
data["c"]=""
cols = data.columns.tolist()
data = data[cols]
data.to_csv('fueln2.csv',sep=',')

file=open('fueln2.csv')
data =pd.read_csv(file,sep=',')

for i in xrange(0,len(data['fuel'])):
    x=data['fuel'][i]
    if x==1:
       data['f'][i]='Bio-power'

    if x==2:
        data["f"][i]='Coal'
    if x==3:
        data["f"][i]='Gas'
    if x==4:
        data["f"][i]='Nuclear'
    if x==5:
        data["f"][i]='Oil'
print data["f"]
for i in xrange(0,len(data['cooling'])):
    x=data['cooling'][i]
    if x==1:
       data['c'][i]='ST-OT'

    if x==2:
        data["c"][i]='ST-RC'
    if x==3:
        data["c"][i]='ST-DC'
    if x==4:
        data["c"][i]='CC-OT'
    if x==5:
        data["c"][i]='CC-RC'
    if x==6:
        data["c"][i]='CC-DC'

print data["c"]
data.to_csv('fueln2.csv',sep=',')
