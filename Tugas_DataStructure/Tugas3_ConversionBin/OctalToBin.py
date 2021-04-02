'''
Created on Apr 1, 2021

@author: User
'''
class convertOctalToBiner :
    def StringInput(self):
        octString = input("Masukkan Nilai Octal yang ingin dikonversi (0-7): ")
        return octString
    
    def ConvertString(self,octString):
        scale = 8 ## equals to hexadecimal
        num_of_bits = 8
        hasilKonversi = bin(int(octString, scale))[2:].zfill(num_of_bits)
        return hasilKonversi
    
    def CetakHasil(self,octString,hasilKonversi):
        print (f"Nilai Octal {octString} adalah {hasilKonversi}")
        
