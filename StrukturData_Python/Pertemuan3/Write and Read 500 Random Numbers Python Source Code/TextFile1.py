'''
Created on Mar 15, 2021

@author: indrabt
'''
class TextFile1 :
    def OpenFile(self):
        myTextFile = open("myfile.txt","w")
        return myTextFile
    
    def WriteToTheTextFile(self,myTextFile):
        myTextFile.write("First Line. Second Line\n")
        return myTextFile
    
    def CloseTextFile(self,myTextFile):
        myTextFile.close()
        return myTextFile
        
