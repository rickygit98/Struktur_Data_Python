'''
Created on Mar 16, 2021

@author: User
'''
import random
class RandomNumber:
    def OpenFile(self):
        myTextFile = open("random.txt","w")
        return myTextFile
    
    def WriteToTheTextFile(self,myTextFile):
        for i in range(1, 501):
            myTextFile.write(str(random.randint(1, 500)))
            myTextFile.write(" ")
            if i > 1 and i % 10 == 1 :
                myTextFile.write("\n")
        return myTextFile
    
    def CloseTextFile(self,myTextFile):
        myTextFile.close()
        return myTextFile
    