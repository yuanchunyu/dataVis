import pandas as pd  
import numpy as np 
import os
import csv


f=open('powerplant.csv')
data=pd.read_csv(f,usecols=['place','lon','lat','cooling','fuel','state','f','c'])
#print np.floor((data['latitude']-5)/0.05),(data['longitude']+138)/0.05
#print np.floor((data['latitude'].stype(float)-5)/0.05).astype(str)
data['dischargefile']=np.floor((data['lat']-5)/0.05).astype(int).astype(str)+'_'+np.floor((data['lon']+138)/0.05).astype(int).astype(str)+'.tsv'
f2=open('K05data.csv')
x=pd.read_csv(f2,sep=',')
x.columns=['idc','place']




file=open('k05yearspower.csv','w')
writer=csv.writer(file)

for j in xrange(0,len(data['place'])):
       for i in xrange(0,len(x)):
         if x['place'][i]==data['place'][j]:
             varis=[]
             varis.append(data['place'][j])
             varis.append(data['lon'][j])
             varis.append(data['lat'][j])
             varis.append(data['cooling'][j])
             varis.append(data['fuel'][j])
             varis.append(data['state'][j])
             varis.append(data['f'][j])
             varis.append(data['c'][j])
             varis.append(x['idc'][i])
             writer.writerow(varis)
             print j
file.close()

f=open('k05yearspower.csv')
data=pd.read_csv(f,sep=',')
data.columns=['place','lon','lat','cooling','fuel','state','f','c','idc']
x=data[data['idc']==0]
#print x
x.to_csv('k05idc0.csv')
a=data[data['idc']==1]
#print x
a.to_csv('k05idc1.csv')
b=data[data['idc']==2]
#print x
b.to_csv('k05idc2.csv')
c=data[data['idc']==3]
#print x
c.to_csv('k05idc3.csv')
d=data[data['idc']==4]
#print x
d.to_csv('k05idc4.csv')
e=data[data['idc']==5]
#print x
e.to_csv('k05idc5.csv')

data.to_csv('k05yearspower.csv')

