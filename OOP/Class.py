class Talaba:
    def __init__(self, ism, familya, tyil):
        self.name=ism
        self.surename=familya
        self.born=tyil
        
    def get_lastname(self):
        return self.surename
        
    def get_age(self, yil):
        return yil-self.born
    
    def tanishtir(self):
        return (f"ISMIM {self.name} {self.surename}, tugilgan yilim {self.born}")

talaba1=Talaba("maqsad", "rahimov", 2006)
talaba2=Talaba("umrbek", "nargi", 2008)
talaba3=Talaba("rahim", "gren", 2100)
talaba4=Talaba("joha", "aslkj", 2010)
talaba5=Talaba("usmon", "ummon", 2004)