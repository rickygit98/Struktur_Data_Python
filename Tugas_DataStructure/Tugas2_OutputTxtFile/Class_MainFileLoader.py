'''
Created on Mar 23, 2021

@author: User
'''
from Tugas2_OutputTxtFile.Class_OpenFile import OpenFile
from Tugas2_OutputTxtFile.Class_ReadFile import ReadOutputFile
from Tugas2_OutputTxtFile.JawabanSoal_1 import WriteJawabanSoal1
from Tugas2_OutputTxtFile.JawabanSoal_2 import WriteJawabanSoal2
from Tugas2_OutputTxtFile.JawabanSoal_3 import WriteJawabanSoal3
from Tugas2_OutputTxtFile.JawabanSoal_4 import WriteJawabanSoal4
from Tugas2_OutputTxtFile.JawabanSoal_5 import WriteJawabanSoal5

print("="*50)
print("Program Tugas txt file Handling")
print("="*50)
print("Note : Saat file belum ada, wajib jalankan dulu pilihan nomor 1")
print()
print("0. Buat file baru output.txt")
print("1. Write Jawaban Soal nomor 1 - Deret Bilangan")
print("2. Write Jawaban Soal nomor 2 - Deret Fibonanci")
print("3. Write Jawaban Soal nomor 3 - Deret Bilangan Genap")
print("4. Write Jawaban Soal nomor 4 - Deret Bilangan Ganjil")
print("5. Write Jawaban Soal nomor 5 - Pola Segitiga")
print("9. Cetak Isi file output.txt saat ini ke Console")
print()


msg_success = "file berhasil ditulis"
msg_failed = "file gagal ditulis"

ulang = "y"
while(ulang == "y"):
    pilihan = int(input("Pilihan anda (0/1/2/3/4/5/9) :"))
    print()
    if pilihan == 0 :
        OpenFile = OpenFile()
        myOutputFile = OpenFile.OpenOutputFile()
        OpenFile.WriteOutputFile(myOutputFile)
        OpenFile.CloseOutputFile(myOutputFile)
        print(msg_success)
        print()
        
    elif pilihan == 1 :
        jawabanSoal1 = WriteJawabanSoal1()
        myOutputFile = jawabanSoal1.OpenOutputFile()
        n = int(input("1.Masukkan batas deret angka: "))
        jawabanSoal1.WriteOutputFile(myOutputFile, n)
        print(msg_success)
        print()
        
    elif pilihan == 2 :
        jawabanSoal2 = WriteJawabanSoal2()
        myOutputFile = jawabanSoal2.OpenOutputFile()
        n = int(input("2.Masukkan batas deret angka Fibonanci: "))
        jawabanSoal2.WriteOutputFile(myOutputFile, n)
        print(msg_success)   
        print()
        
    elif pilihan == 3 :
        jawabanSoal3 = WriteJawabanSoal3()
        myOutputFile = jawabanSoal3.OpenOutputFile()
        n = int(input("3.Masukkan banyaknya bilangan Genap yang ingin ditampilkan: "))
        jawabanSoal3.WriteOutputFile(myOutputFile, n)
        print(msg_success)
        print()
        
    elif pilihan == 4 :
        jawabanSoal4 = WriteJawabanSoal4()
        myOutputFile = jawabanSoal4.OpenOutputFile()
        n = int(input("4.Masukkan banyaknya bilangan Ganjil yang ingin ditampilkan: "))
        jawabanSoal4.WriteOutputFile(myOutputFile, n)
        print(msg_success)
        print()
        
    elif pilihan == 5 :
        jawabanSoal5 = WriteJawabanSoal5()
        myOutputFile = jawabanSoal5.OpenOutputFile()
        n = int(input("5.Masukkan nilai - n bintang : "))
        jawabanSoal5.WriteOutputFile(myOutputFile, n)
        print(msg_success)
        print()
        
    elif pilihan == 9 :
        writeToConsole = ReadOutputFile()
        myOutputFile = writeToConsole.OpenOutputFile()
        writeToConsole.ReadOutputFile(myOutputFile)
        writeToConsole.CloseOutputFile(myOutputFile)
        print()
        
    else :
        print("Pilihan tidak ada")
        print()
    
    print("="*50)
    ulang = input("Apakah anda ingin mengulang?(Y/N)")
    ulang = ulang.lower()
    print()
    
print("Keluar Program - Terima Kasih!")