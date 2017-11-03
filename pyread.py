import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        filename1 = child[36:]
        createfile1=open("/home/yuanchunyu/yuanvis/dataVis/td1/"+filename1,'a+')
        
        fd=open(child,'r')
        for line in fd.readlines()[9132:14976]:
            createfile1.writelines('%s' % (line))
        fd.close()
        createfile1.close()
        print child[36:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/yuanvis/dataVis/td/"
    eachFile(filePath)
    
