import os
import pandas as pd




def copyFileCooling(filePath,dataName,folder):
    f=open(dataName)
    #print dataName
    data=pd.read_csv(f)
    #pathDir = os.listdir(filePath)
    i=0
    #print data
    filena=data['nrel_id']
    for row in filena:
        print row
        row1=str(row)+".csv"
        print row1
        row2=str(row)+".tsv"
        path = "/home/yuanchunyu/dataVis1/chooseFile/"+folder+"/"+row1
        if os.path.isfile(path):
           continue
        else:
           createfile1=open(path,'a+')
           fd=open("/home/yuanchunyu/dataVis1/ts1/"+row2,'r')
           for line in fd.readlines():
               createfile1.writelines('%s' % (line))
           fd.close()
           createfile1.close()
        #print child[34:]
        i+=1
    print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/ts1/"
    dataName="./chooseFile/cooling1.csv"
    folder="tsc1"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling2.csv"
    folder="tsc2"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling3.csv"
    folder="tsc3"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling4.csv"
    folder="tsc4"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling5.csv"
    folder="tsc5"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/cooling6.csv"
    folder="tsc6"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel1.csv"
    folder="tsf1"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel2.csv"
    folder="tsf2"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel3.csv"
    folder="tsf3"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel4.csv"
    folder="tsf4"
    copyFileCooling(filePath,dataName,folder)
    dataName="./chooseFile/fuel5.csv"
    folder="tsf5"
    copyFileCooling(filePath,dataName,folder)
    
