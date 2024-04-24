# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:53:42 2024

@author: фвьшт

"""

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
ismlar=["maqsad","farruh","ogabek","raulbek"]
katta_harf(ismlar)
print(ismlar)

# 2)def katta_harf(matnlar):
#     matnlar=matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar=["maqsad","farruh","ogabek","raulbek"]
# yangi=katta_harf(ismlar)
# print(ismlar)
# print(yangi)

#Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
#foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
        
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
