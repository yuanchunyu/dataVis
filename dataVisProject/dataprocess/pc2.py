import os
import pandas as pd
def eachFile(filepath,folder):
    pathDir = os.listdir(filepath)
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        #data=pd.read_csv(child)
        cov = pd.read_csv(child, sep='\t', 
                  names = ["time", "count"]) 
        print child,cov['count'].max(),cov['count'].min()
        ma=cov['count'].max()
        mi=cov['count'].min()
        cov['countnew']=(cov['count']-mi)/(ma-mi)
        cov.to_csv("/home/yuanchunyu/dataVis1/chooseFile/"+folder+"/"+child[42:], sep='\t',header=False)
        #fd=open(child,'r')
        #for line in fd.readlines()[9132:14976]:
         #   createfile1.writelines('%s' % (line))
        #fd.close()
        #createfile1.close()
        #print child[34:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tcsv/"
    folder="tcsn"
    eachFile(filePath,folder)
    
