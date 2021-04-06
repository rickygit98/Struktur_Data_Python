'''
Created on Apr 5, 2021

@author: User
'''

class LinearSearch:
    def InputNilaiN(self):
        n = int(input("Masukkan nilai n = "))
        while n > 10 or n < 0 :
            print("Nilai n antara 1-10")
            n = int(input("Masukkan nilai n = "))
        return n
    
    def InputBilanganCari(self):
        cari = int(input("Masukkan bilangan yang mau dicari didalam list = "))
        return cari
    
    def InputBilanganList(self, n):
        ListBilangan = []
        for i in range(0, n):
            temp = int(input("Masukkan bilangan ke "+ str(i + 1) + " = "))
            ListBilangan.append(temp)
        return ListBilangan
    
    def HasilSearch(self, cari, ListBilangan):
        HasilCari = False
        for i in ListBilangan:
            if cari == i:
                HasilCari = True
                break
        return HasilCari

Linear = LinearSearch()
n = Linear.InputNilaiN()
ListBilangan = Linear.InputBilanganList(n)
cari = Linear.InputBilanganCari()
HasilPencarian = Linear.HasilSearch(cari, ListBilangan)
if HasilPencarian :
    print("Hasil pencarian ditemukan didalam list")
else :
    print("Hasil pencarian tidak ditemukan didalam list")


