# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
final = open('mean_var16.csv' , 'r')

data = [line.strip().split(',') for line in final]
feature = [[x for x in row[1:]] for row in data]
print feature
fe=np.array(feature)
print fe.shape
#kmeans 
clf = KMeans(n_clusters=6)
s = clf.fit(feature)
print s

#9 center
print clf.cluster_centers_

label=np.array(clf.labels_)
file=open('K15data.csv','w')
writer=csv.writer(file)

for i in xrange(0,len(label)):
    varis=[]
    varis.append(label[i])
    varis.append(data[i][0])
    writer.writerow(varis)
    print label[i],data[i][0]
file.close();
print label.shape,

#each label for sample



print clf.labels_


#check k , lower better
print clf.inertia_

#predict
print clf.predict(feature[1:])



file=open('testK15.csv','w')
writer=csv.writer(file)
#check k value
for i in range(1,30,1):
    varis=[]
    clf = KMeans(n_clusters=i)
    s = clf.fit(feature)
    varis.append(i)
    varis.append(clf.inertia_)
    print i,clf.inertia_
    writer.writerow(varis)
file.close() 
file=open('testK15.csv')
data=pd.read_csv(file,sep=',')
data.columns=['i','k']
x=np.array(data['i'])
y=np.array(data['k'])

plt.plot(x,y,'ro',linestyle='dashed')
plt.title("k value change 16 years data")
plt.show()

