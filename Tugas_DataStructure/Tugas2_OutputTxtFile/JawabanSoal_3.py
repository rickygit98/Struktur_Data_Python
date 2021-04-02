'''
Created on Mar 23, 2021

@author: User
'''
class WriteJawabanSoal3 :
    def OpenOutputFile(self):
        myOutputFile = open("output.txt","a")
        return myOutputFile  
    
    def WriteOutputFile(self,myOutputFile,n):
        myOutputFile.write(f"--- Jawaban Soal 3 Bilangan Genap (Even Number) ---\n")
        
        awal = 0
        counter = 0
        while (counter < n):  
            myOutputFile.write(f"{awal} ")
            awal += 2
            counter+=1
            
        myOutputFile.write(f" \n")
        return myOutputFile
    
    def CloseOutputFile(self,myOutputFile):
        close = myOutputFile.close()
        return close
