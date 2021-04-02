'''
Created on Mar 8, 2021

@author: indrabt
'''
class SecondQuestion:
    def InputKalimat(self):
        kalimat = input("Masukkan kalimat = ")
        kalimat = kalimat.lower()
        return kalimat
    def ReplaceVocalLetter(self, kalimat):
        kalimat = kalimat.replace("a","*")
        kalimat = kalimat.replace("i","*")
        kalimat = kalimat.replace("u","*")
        kalimat = kalimat.replace("e","*")
        kalimat = kalimat.replace("o","*")
        return kalimat
    def CetakKalimat(self, kalimat):
        print(kalimat)

        
    