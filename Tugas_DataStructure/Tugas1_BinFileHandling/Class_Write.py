'''
Created on Mar 19, 2021

@author: User
'''
from sys import byteorder

class WriteBinFile :
    def OpenBinFile(self):
        myBinFile = open("Hello.jpg","wb")
        return myBinFile   
    
    def WriteToTheBinFile(self,myBinFile,bytes):
        for b in bytes:
            myBinFile.write(b.to_bytes(1,byteorder="big"))
        return myBinFile
    
    def CloseBinFile(self,myBinFile):
        close = myBinFile.close()
        return close