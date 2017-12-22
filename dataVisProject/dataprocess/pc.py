import pandas as pd
import numpy as np
import os
import csv

def c_mean_var(filepath, savefile):
    
    pathDir =  pathDir = os.listdir(filepath)
    file=open(savefile,'w')
    writer=csv.writer(file)
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        varis=[]
        #cov = pd.read_csv(child ) 
        ids= child[42:-4]
        data=pd.read_csv(child,sep='\t')
        data.columns=["id","time","count","countnew"]
        data=data[0:2192]
        print len(data)
        a=np.array(data["countnew"])
        mean=a.mean()
        var=a.var()
        print len(a)
        varis.append(ids)
        varis.append(mean)
        varis.append(var)
        x=0
        max=data["countnew"].max()
        for i in a:
            if i==max:  
                x+=1
        fre=float(x)/2192
        varis.append(fre)
        x=0
        y=1
        for i  in xrange(1, len(a)):
       
            if a[i] > a[i - 1]:
                y = y + 1
            else:
                if y>=3:
                   x+=y
                y = 1
        print ids
        incr= float(x)/2192
        varis.append(incr)
        x1=0
        y1=1
        for i  in xrange(1, len(a)):
       
            if a[i] < a[i - 1]:
                  y1 = y1 + 1
            else:
                if y1>=3:
                   x1+=y1
                y1 = 1
        decr =float(x1)/2192
   
        varis.append(decr)
        writer.writerow(varis)
        print varis
    file.close()





if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tcsn/"
    savefile="mean_var06.csv"
    c_mean_var(filePath,savefile)




#import pandas as pd

#data = pd.read_csv("path/to/file.txt", sep='\t', header=None)
#data.columns = ["Sequence", "Start", "End", "Coverage"]
