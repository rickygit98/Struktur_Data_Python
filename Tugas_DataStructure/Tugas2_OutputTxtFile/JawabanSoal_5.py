'''
Created on Mar 23, 2021

@author: User
'''
class WriteJawabanSoal5 :
    def OpenOutputFile(self):
        myOutputFile = open("output.txt","a")
        return myOutputFile  
    
    def WriteOutputFile(self,myOutputFile,n):
        myOutputFile.write(f"--- Jawaban Soal 5 Pola Segitiga ---\n")
        
        for i in range(1,n+1):
            myOutputFile.write('*'*i+"\n")
            
        
        myOutputFile.write(f" \n")
        return myOutputFile
    
    def CloseOutputFile(self,myOutputFile):
        close = myOutputFile.close()
        return close