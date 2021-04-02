'''
Created on Mar 19, 2021

@author: User
'''
from Tugas1_BinFileHandling.Class_Write import WriteBinFile
from Tugas1_BinFileHandling.Class_Read import ReadBinFile
from Tugas1_BinFileHandling.Class_RandomByte import RandomByteGenerator
import operator
from random import seed

print("======================================================")
print("Program Bin file Handling")
print("======================================================")
print("1. Program untuk menulis ke bin file")
print("2. Program untuk membaca isi bin file")

pilihan = int(input("Pilihan anda (1/2) :"))


#Generate Random Bytes
seed(1)
n = RandomByteGenerator()
bytes = n.RandomBytes(20)
#n.DisplayBytes(bytes)

if pilihan == 1 :
    bin = WriteBinFile()
    fileBin = bin.OpenBinFile()
    fileBin = bin.WriteToTheBinFile(fileBin,bytes)
    bin.CloseBinFile(fileBin)
    
elif pilihan == 2 :
    bin = ReadBinFile()
    fileBin = bin.OpenBinFile()
    fileBin = bin.ReadBinFile(fileBin)
    bin.CloseBinFile(fileBin)
    
else :
    print("Pilihan tidak ada")