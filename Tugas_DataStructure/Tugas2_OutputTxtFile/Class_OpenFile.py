'''
Created on Mar 23, 2021

@author: User
'''
class OpenFile :
    def OpenOutputFile(self):
        myOutputFile = open("output.txt","w")
        return myOutputFile  
    
    def WriteOutputFile(self,myOutputFile):
        myOutputFile.write(f"--- TUGAS 2 File Handling ---\n")
        myOutputFile.write("\n")
        return myOutputFile
    
    def CloseOutputFile(self,myOutputFile):
        close = myOutputFile.close()
        return close
