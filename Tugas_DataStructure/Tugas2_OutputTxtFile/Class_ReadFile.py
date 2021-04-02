'''
Created on Mar 23, 2021

@author: User
'''
class ReadOutputFile :

    def OpenOutputFile(self):
        myOutputFile = open("output.txt","r")
        return myOutputFile
    
    def ReadOutputFile(self,myOutputFile):
 
        fileContent = myOutputFile.read()
        
        print("")
         
        print(f"{fileContent}")    
        return fileContent
     
    def CloseOutputFile(self,myOutputFile):
        myOutputFile.close()
        return myOutputFile

