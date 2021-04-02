'''
Created on Mar 29, 2021

@author: indrabt
'''
class ContohDictionary:
    def cobaDictionary(self):
        info = {}
        info["Name"] = "Sandy"
        info["occupation"] = "hacker"
        indeks = info.get("Job", None)
        print(indeks)