'''
Created on Mar 22, 2021

@author: User
'''

class WriteJawabanSoal1 :
    def OpenOutputFile(self):
        myOutputFile = open("output.txt","a")
        return myOutputFile  
    
    def WriteOutputFile(self,myOutputFile,n):
        myOutputFile.write(f"--- Jawaban Soal 1 Deret angka ---\n")
        for i in range (n):   
            myOutputFile.write(f"{i+1} ")
        
        myOutputFile.write(f" \n")
        return myOutputFile
    
    def CloseOutputFile(self,myOutputFile):
        close = myOutputFile.close()
        return close