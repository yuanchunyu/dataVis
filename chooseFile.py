import os
import pandas as pd




def copyFileCooling(filePath,dataName,folder):
    f=open(dataName)
    data=pd.read_csv(f)
    #pathDir = os.listdir(filePath)
    #i=0
    #print data
    filena=data['dischargefile']
    for row in filena:
        print row[0:-3]
        row1=row[0:-3]+"csv"
        path = "/home/yuanchunyu/dataVis1/chooseFile/"+folder+"/"+row1
        if os.path.isfile(path):
           continue
        else:
           createfile1=open(path,'a+')
           fd=open("/home/yuanchunyu/dataVis1/td1/"+row,'r')
           for line in fd.readlines():
               createfile1.writelines('%s' % (line))
           fd.close()
           createfile1.close()
        #print child[34:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/td1/"
    dataName="./chooseFile/cooling1.csv"
    folder="tdc1"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling2.csv"
    folder="tdc2"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling3.csv"
    folder="tdc3"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling4.csv"
    folder="tdc4"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling5.csv"
    folder="tdc5"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling6.csv"
    folder="tdc6"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel1.csv"
    folder="tdf1"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel2.csv"
    folder="tdf2"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel3.csv"
    folder="tdf3"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel4.csv"
    folder="tdf4"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel5.csv"
    folder="tdf5"
    copyFileCooling(filePath,dataName,folder)
    
