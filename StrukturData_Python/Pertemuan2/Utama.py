'''
Created on Mar 8, 2021

@author: indrabt
'''
from FirstQuestion import FirstQuestion
from SecondQuestion import SecondQuestion

print("===========================================================")
print("1. Program menghitung huruf vokal pada kalimat")
print("2. Program mengganti huruf vokal menjadi *")
print("===========================================================")
pilihan = int(input("Pilihan anda (1/2) : "))
if pilihan == 1 :
    FirstQuestion = FirstQuestion()
    kalimat = FirstQuestion.InputKalimat()
    jumlahHurufVokal = FirstQuestion.HitungHurufVokal(kalimat)
    FirstQuestion.CetakHurufVokal(jumlahHurufVokal)
elif pilihan == 2 :
    SecondQuestion = SecondQuestion()
    kalimat = SecondQuestion.InputKalimat()
    kalimat = SecondQuestion.ReplaceVocalLetter(kalimat)
    SecondQuestion.CetakKalimat(kalimat)
else :
    print("pilihan yang anda pilih tidak ada ")