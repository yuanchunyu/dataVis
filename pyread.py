import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        filename1 = child[34:]
        createfile1=open("/home/yuanchunyu/dataVis/td1/"+filename1,'a+')
        fd=open(child,'r')
        for line in fd.readlines()[9132:14976]:
            createfile1.writelines('%s' % (line))
        fd.close()
        createfile1.close()
        print child[34:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/home/yuanchunyu/dataVis/td/"
    eachFile(filePath)
    
