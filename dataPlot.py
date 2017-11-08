import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import os



def eachFile(filepath):
    pathDir = os.listdir(filepath)
    #i=0
    plt.figure(figsize=(20,10))
    x=0
    t1=np.arange(0, 5843, 1) 
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        #data=pd.read_csv(child)
        cov = pd.read_csv(child, sep='\t', 
                    names = ["time", "count","countnew"]) 
        ma=cov['countnew'][1:].astype(float)
        ma=np.array(ma)
        print len(ma) ,len(t1),child    
        plt.plot(t1, ma+x, c=np.random.rand(3,1), lw=2)
        x+=3.5
        #fd=open(child,'r')
        #for line in fd.readlines()[9132:14976]:
         #   createfile1.writelines('%s' % (line))
        #fd.close()
        #createfile1.close()
        #print child[34:]
       # i+=1
    plt.show()
if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc5n/"
    eachFile(filePath)
