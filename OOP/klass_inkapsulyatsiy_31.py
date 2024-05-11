# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:26:18 2024

@author: фвьшт
"""


from uuid import uuid4
class Avto:
    __num_avto=0
    def __init__(self, make , model,rang,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            print("Moshina kilometrini kamaytirib bo'lmaydi!!!")
            
avto1=Avto("GM","MOLIBU", "QORA", 2021, 20000, 1000)
avto2=Avto("GM","TREKKER", "OQ", 2022, 30000, 500)