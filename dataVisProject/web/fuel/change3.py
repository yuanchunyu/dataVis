import numpy as np
import pandas as pd

file=open('fueln2.csv')
data =pd.read_csv(file,sep=',')
#print data["state"]
data["state"]=""
cols = data.columns.tolist()
data = data[cols]
data.to_csv('fueln2.csv',sep=',')

file=open('fueln2.csv')
data =pd.read_csv(file,sep=',')
fil=open('powerplant.csv')
dat =pd.read_csv(fil,sep=',')
dd=data['place']
for i in xrange(0,len(dd)):
  for j in xrange(0,len(dat['place'])):
     if dd[i]==dat['place'][j]:
         print data['state'][i]
         data['state'][i]=dat['state'][j]
     

print data["state"]
data.to_csv('fueln2.csv',sep=',')
