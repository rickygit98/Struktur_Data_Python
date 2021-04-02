'''
Created on Mar 29, 2021

@author: indrabt
'''
class ContohList :
    def CetakList(self):
        angka = range(0, 10)
        print("Cetak angka cara pertama di list menggunakan for in range")
        for i in range(0, 10):
            print(angka[i], end = " ")
        print()
        
        print("Cetak angka cara kedua di list menggunakan for in")
        for temp in angka :
            print(temp, end = " ")
        
        