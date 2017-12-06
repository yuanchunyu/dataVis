import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    print pathDir
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        filename1 = child[29:]
        #print filename1
        #print child
        createfile1=open("/home/yuanchunyu/dataVis1/ts_5years/"+filename1,'a+')
        fd=open(child,'r')
        for line in fd.readlines()[9132:11324]:
            createfile1.writelines('%s' % (line))
        fd.close()
        createfile1.close()
        print child[29:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis1/ts/"
    print filePath
    eachFile(filePath)
    
