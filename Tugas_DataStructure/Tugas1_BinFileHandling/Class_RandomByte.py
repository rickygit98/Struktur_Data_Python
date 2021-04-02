'''
Created on Mar 19, 2021

@author: User
'''
import random
import operator
from random import randint, randrange, seed

class RandomByteGenerator:
    def RandomBytes(self,size):
        bytes=[]
        for i in range(size):
            bytes.append(randrange(0,255))
        return bytes

    def DisplayBytes(self,bytes):
        print("=======")
        for index,item in enumerate(bytes):
            print(f"{index}. {item} ({hex(item)})")
        print("=======")