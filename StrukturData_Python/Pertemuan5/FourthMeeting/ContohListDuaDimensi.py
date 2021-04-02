'''
Created on Mar 29, 2021

@author: indrabt
'''
class ContohListDuaDimensi:
    def CetakListDuaDimensi(self):
        angka = [[1,2],
                 [3,4],
                 [5,6],
                 [7,8],
                 [9,0]
                ]
        print("Cetak angka dua dimensi di list menggunakan for in")
        for temp1 in angka :
            print(temp1, end =  " ")
#             for temp2 in temp1:
#                 print(temp2, end = " ")