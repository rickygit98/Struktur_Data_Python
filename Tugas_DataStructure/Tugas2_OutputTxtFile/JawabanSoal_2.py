'''
Created on Mar 23, 2021

@author: User
'''
class WriteJawabanSoal2 :
    def OpenOutputFile(self):
        myOutputFile = open("output.txt","a")
        return myOutputFile  
    
    def WriteOutputFile(self,myOutputFile,n):
        myOutputFile.write(f"--- Jawaban Soal 2 Deret Fibonanci ---\n")
        d1 = 0
        d2 = 1
        
        for i in range (n):   
            if (d1 <= n):
                myOutputFile.write(f"{d1} ")
                d3 = d2 + d1
                d1 = d2
                d2 = d3
        
        myOutputFile.write(f" \n")
        return myOutputFile
    
    def CloseOutputFile(self,myOutputFile):
        close = myOutputFile.close()
        return close
