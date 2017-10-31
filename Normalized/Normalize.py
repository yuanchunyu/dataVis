
# -*- coding: utf-8 -*-
"""
    Created on Mon Oct 30 03:43:32 2017
    
    @author: Moti
    """

import pandas as pd
import os

pathDir = os.listdir("/Users/Moti/Documents/GitHub/dataVis/td1/")
DF = pd.DataFrame()
min = 0
max = 268494.41

for eachDir in pathDir:
    child = os.path.join('%s%s' %("/Users/Moti/Documents/GitHub/dataVis/td1/", eachDir))
    filename = child[41:].translate(None, '.tsv')
    print filename
    df = pd.read_csv(child, sep='\t', header= None)
    #latlon = eachDir.translate(None, '.tsv')
    df.rename(columns={
              0: 'date',
              1: filename}, inplace = True)

              df.drop(['date'], axis = 1, inplace = True)
              df = df.T
              for i in range (1,5844):
                  val = df.xs(filename)[i]
                  df.xs(filename)[i] = val / max
                  #print df
              normalizedversion = open("/Users/Moti/Documents/GitHub/dataVis/Normalized/"+filename+".csv",'a+')
              df.to_csv(normalizedversion, sep="\t",index = False)
              #DF = DF.append(df)


#All in One csv file
#DF.to_csv("/Users/Moti/Documents/GitHub/dataVis/AllInOne.csv", sep='\t')

