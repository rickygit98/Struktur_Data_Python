'''
Created on Mar 15, 2021

@author: indrabt
'''
class BacaFileRandom :
    def OpenFile(self):
        textFile = open("random.txt","r")
        return textFile
    def WriteTextFileToMonitor(self,textFile):
        fileContent = textFile.read()
        print("Isi file text bilangan random = ",fileContent)
    
    def CloseTextFile(self,textFile):
        textFile.close()
        return textFile    