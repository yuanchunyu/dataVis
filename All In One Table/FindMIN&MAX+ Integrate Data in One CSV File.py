
# -*- coding: utf-8 -*-
"""
    Created on Mon Oct 30 03:43:32 2017
    
    @author: Moti
    """

import pandas as pd
import os

pathDir = os.listdir("/Users/Moti/Documents/GitHub/dataVis/td1/")
DF = pd.DataFrame()

for eachDir in pathDir:
    child = os.path.join('%s%s' %("/Users/Moti/Documents/GitHub/dataVis/td1/", eachDir))
    filename1 = child[34:]
    df = pd.read_csv(child, sep='\t', header= None)
    df.rename(columns={
              0: 'date',
              1: eachDir.translate(None, '.tsv')}, inplace = True)
              df.drop(['date'], axis = 1, inplace = True)
              df = df.T
              #print df
              #print df.values.max()
    DF = DF.append(df)

#print DF
print "max :",DF.values.max(),"min",DF.values.min()
DF.to_csv("/Users/Moti/Documents/GitHub/dataVis/AllInOne.csv", sep='\t')
