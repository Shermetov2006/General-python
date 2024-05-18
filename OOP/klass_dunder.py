# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:48:51 2024

@author: фвьшт
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:59:03 2024

@author: ПИРМУХАММАД
"""

class Avto:
    def __init__(self, model , rang, korovka,narh,km):
        self.model=model
        self.rang=rang
        self.korovka=korovka
        self.narh=narh
        self.km=km
        
    def repr(self):
        return f"Avto: {self.model} {self.rang}"
    
    def eq(self, y):
        return self.narh==y.narh
    def lt(self,y):
        return self.narh<y.narh
    def le(self, y):
        return self.narh<=y.narh
    
avto1=Avto("Getaur", "qora", "avtamat", 10000, 1000)        
avto2=Avto("Getaur", "qora", "avtamat", 20000, 1000)   


class Avtosalon:
    def __init__(self, name):
        self.name=name
        self.avtolar=[]
        
    def repr(self):
        return f"Avto: {self.name} avtosaloni"
    
    def len(self):
        return len(self.avtolar)
    
    def getitem(self,index):
        return self.avtolar[index]
    def setitem(self,index,qiymat):
        self.avtolar[index]=qiymat
     
    def __call__ (self):
        return [avto for avto in self.avtolar]
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")

salon1=Avtosalon("MaxAvto")
                
              
avto1=Avto("Getaur", "qora", "avtamat", 20000, 1000)
avto2=Avto("malibu", "qora", "avtamat", 20000, 1000)
avto3=Avto("nexia", "qora", "avtamat", 10000, 1000)
salon1.add_avto(avto1,avto2,avto3)