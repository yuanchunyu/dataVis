import pandas as pd  
import numpy as np 

f=open('powerplants.csv')
data=pd.read_csv(f,usecols=['nrel_id','longitude','latitude','cooling','fuel','state'])
#print np.floor((data['latitude']-5)/0.05),(data['longitude']+138)/0.05
#print np.floor((data['latitude'].stype(float)-5)/0.05).astype(str)
data['dischargefile']=np.floor((data['latitude']-5)/0.05).astype(int).astype(str)+'_'+np.floor((data['longitude']+138)/0.05).astype(int).astype(str)+'.tsv'

x=data[data['cooling']==1]
#print x
x.to_csv('cooling1.csv')
a=data[data['cooling']==2]
b=data[data['cooling']==3]
c=data[data['cooling']==4]
d=data[data['cooling']==5]
e=data[data['cooling']==6]
a.to_csv('cooling2.csv')
b.to_csv('cooling3.csv')
c.to_csv('cooling4.csv')
d.to_csv('cooling5.csv')
e.to_csv('cooling6.csv')
x1=data[data['fuel']==1]
#print x
x1.to_csv('fuel1.csv')
a1=data[data['fuel']==2]
b1=data[data['fuel']==3]
c1=data[data['fuel']==4]
d1=data[data['fuel']==5]

a1.to_csv('fuel2.csv')
b1.to_csv('fuel3.csv')
c1.to_csv('fuel4.csv')
d1.to_csv('fuel5.csv')


data.to_csv('addFileName.csv')
