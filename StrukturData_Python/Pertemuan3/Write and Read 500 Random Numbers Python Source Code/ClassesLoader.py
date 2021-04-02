'''
Created on Mar 15, 2021

@author: indrabt
'''
from TextFile1 import TextFile1
from TextFile2 import TextFile2
from RandomNumber import RandomNumber
from BacaFileRandom import BacaFileRandom

print("======================================================")
print("Program demo text file")
print("======================================================")
print("1. Program untuk menulis ke file text")
print("2. Program untuk membaca isi file text")
print("3. Program untuk menulis isi file text bilangan random")
print("4. Program membaca isi file text bilangan random")
print("======================================================")
pilihan = int(input("Pilihan anda (1/2/3/4) :"))
if pilihan == 1 :
    myTextFile = TextFile1()
    textFileDemo = myTextFile.OpenFile()
    textFileDemo = myTextFile.WriteToTheTextFile(textFileDemo)
    textFileDemo = myTextFile.CloseTextFile(textFileDemo)
elif pilihan == 2 :
    myTextFile = TextFile2()
    readTextFileDemo = myTextFile.OpenFile()
    myTextFile.WriteTextFileToMonitor(readTextFileDemo)
    readTextFileDemo = myTextFile.CloseTextFile(readTextFileDemo)
elif pilihan == 3 :
    myTextFile = RandomNumber()
    randomFileDemo = myTextFile.OpenFile()
    randomFileDemo = myTextFile.WriteToTheTextFile(randomFileDemo)
    randomFileDemo = myTextFile.CloseTextFile(randomFileDemo)
elif pilihan == 4 :
    myTextFile = BacaFileRandom()
    readRandomFileText = myTextFile.OpenFile()
    myTextFile.WriteTextFileToMonitor(readRandomFileText)
    readRandomFileText = myTextFile.CloseTextFile(readRandomFileText)
else :
    print("Pilihan tidak ada")
