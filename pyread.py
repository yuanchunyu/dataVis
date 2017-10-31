import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    #i=0
    for allDir in pathDir:
        child = os.path.join('%s%s' %(filepath, allDir))
        filename1 = child[34:]
        createfile1=open("/Users/Moti/Documents/GitHub/dataVis/td2/"+filename1,'a+')
        createfile1.writelines('%s' % ("date count"))
        fd=open(child,'r')
        for line in fd.readlines()[9132:14976]:
            createfile1.writelines('%s' % (line))
        fd.close()
        createfile1.close()
        print child[34:]
       # i+=1
    #print i
 

if __name__=='__main__':
    filePath ="/Users/Moti/Documents/GitHub/dataVis/td/"
    eachFile(filePath)
    
