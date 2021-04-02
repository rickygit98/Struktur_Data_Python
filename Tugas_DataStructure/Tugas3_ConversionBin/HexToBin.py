'''
Created on Mar 31, 2021

@author: User
'''

class convertHexaToBiner :
    def StringInput(self):
        hexString = input("Masukkan Nilai Hexa yang ingin dikonversi (0 - f) : ")
        return hexString
    
    def ConvertString(self,hexString):
        scale = 16 ## equals to hexadecimal
        num_of_bits = 8
        hasilKonversi = bin(int(hexString, scale))[2:].zfill(num_of_bits)
        return hasilKonversi
    
    def CetakHasil(self,hexString,hasilKonversi):
        print (f"Nilai Hexadecimal {hexString} adalah {hasilKonversi}")
        
        
