'''
Created on Mar 19, 2021

@author: User
'''
class ReadBinFile :

    def OpenBinFile(self):
        binFile = open("Hello.jpg","rb")
        return binFile
    
    def ReadBinFile(self,binFile):
 
         fileContent = binFile.read()
         
         print("")
         
         print("Isi file bin = ",fileContent,"\n")    
         return binFile
     
    def CloseBinFile(self,binFile):
         binFile.close()
         return binFile