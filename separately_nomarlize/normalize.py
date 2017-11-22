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
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc1/"
    folder="tsc1n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc2/"
    folder="tsc2n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc3/"
    folder="tsc3n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc4/"
    folder="tsc4n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc5/"
    folder="tdc5n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsc6/"
    folder="tsc6n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsf1/"
    folder="tsf1n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsf2/"
    folder="tsf2n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsf3/"
    folder="tsf3n"
    eachFile(filePath,folder)

    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsf4/"
    folder="tsf4n"
    eachFile(filePath,folder)
    filePath ="/home/yuanchunyu/dataVis1/chooseFile/tsf5/"
    folder="tsf5n"
    eachFile(filePath,folder)
    
