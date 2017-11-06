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
        cov.to_csv("/home/yuanchunyu/dataVis1/chooseFile/"+folder+"/"+child[42:], sep='\t')
        #fd=open(child,'r')
        #for line in fd.readlines()[9132:14976]:
         #   createfile1.writelines('%s' % (line))
        #fd.close()
        #createfile1.close()
        #print child[34:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc1/"
    folder="tdc1n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc2/"
    folder="tdc2n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc3/"
    folder="tdc3n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc4/"
    folder="tdc4n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc5/"
    folder="tdc5n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdc6/"
    folder="tdc6n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdf1/"
    folder="tdf1n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdf2/"
    folder="tdf2n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdf3/"
    folder="tdf3n"
    eachFile(filePath,folder)

    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdf4/"
    folder="tdf4n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tdf5/"
    folder="tdf5n"
    eachFile(filePath,folder)
    
