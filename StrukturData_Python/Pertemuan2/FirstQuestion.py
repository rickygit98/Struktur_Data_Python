'''
Created on Mar 8, 2021

@author: indrabt
'''
class FirstQuestion:
    def InputKalimat(self):
        kalimat = input("Masukkan kalimat = ")
        kalimat = kalimat.lower()
        return kalimat
    
    def HitungHurufVokal(self, kalimat):
        jumHurufA = kalimat.count("a")
        jumHurufI = kalimat.count("i")
        jumHurufU = kalimat.count("u")
        jumHurufE = kalimat.count("e")
        jumHurufO = kalimat.count("o")
        total = jumHurufA + jumHurufI + jumHurufU + jumHurufE + jumHurufO
        jumHurufVokal = [jumHurufA, jumHurufI, jumHurufU, jumHurufE, jumHurufO, total]
        return jumHurufVokal
    
    def CetakHurufVokal(self,jumHurufVokal):
        print("Jumlah huruf vokal = ", jumHurufVokal[5])
        print("Jumlah huruf a = ",jumHurufVokal[0])
        print("Jumlah huruf i = ",jumHurufVokal[1])
        print("Jumlah huruf u = ",jumHurufVokal[2])
        print("Jumlah huruf e = ",jumHurufVokal[3])
        print("Jumlah huruf o = ",jumHurufVokal[4])
        