'''
Created on Apr 1, 2021

@author: User
'''
from Tugas3_ConversionBin.HexToBin import convertHexaToBiner
from Tugas3_ConversionBin.OctalToBin import convertOctalToBiner

print("="*50)
print("Program Konversi Angka")
print("="*50)
print()
print("1. Konversi Hexadecimal ke Biner")
print("2. Konversi Octal ke Biner")
print()

ulang = "y"
while(ulang == "y"):
    pilihan = int(input("Pilihan anda (1 / 2) :"))
    print()
    if pilihan == 1 :
        hexa = convertHexaToBiner()
        hexString = hexa.StringInput()
        hasilKonversi = hexa.ConvertString(hexString)
        hexa.CetakHasil(hexString,hasilKonversi)
                
    elif pilihan == 2 :                
        octal = convertOctalToBiner()
        octString = octal.StringInput()
        hasilKonversi = octal.ConvertString(octString)
        octal.CetakHasil(octString,hasilKonversi)
        
    else :
        print("Pilihan tidak ada")
        print()
    
    print("="*50)
    ulang = input("Apakah anda ingin mengulang?(Y/N)")
    ulang = ulang.lower()
    print()
    
print("Keluar Program - Terima Kasih!")