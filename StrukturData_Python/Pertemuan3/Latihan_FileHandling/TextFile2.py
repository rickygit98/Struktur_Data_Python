'''
Created on Mar 16, 2021

@author: User
'''
class TextFile2 :
    def OpenFile(self):
        textFile = open("myfile.txt","r")
        return textFile
    def WriteTextFileToMonitor(self,textFile):
        fileContent = textFile.read()
        print("Isi file text = ",fileContent)
    
    def CloseTextFile(self,textFile):
        textFile.close()
        return textFile