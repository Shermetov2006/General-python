# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:57:12 2024

@author: PITMUHAMMAD
"""
#1)def tyil(ism,yosh,hozirgi_yil=2024):
#     """Foydalanuvchi ismi va yoshini so'rab, 
#     uning tug'ilgan yilini hisoblaydigan funksiya yozing."""
#     print(f'{ism} {hozirgi_yil-yosh}-yil')
# tyil("javohir",17)

# 2)# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")
# kv_kub(-4)

#3) def son(a,b,c):
#     max = a
#     if b>= max:
#         max = b
#     if c>=max:
#         max = c
#     return max

# son(12,15,24)


#4) def aylana_r(radius,pi=3.1415):
#     aylana={'radius': radius,
#             'diametr':2*radius,
#             'perimetr':2*pi*radius,
#             'yuza': pi*radius**2
#             }
#     return aylana

# aylana_r(6)

#5)
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# tub_sonlar_top(1,20)
    
#6)
# def fibonachi(n):
#     sonlar=[]
#     for i in range(n):
#         if i==0 or i==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[i-1]+sonlar[i-2])
#     return sonlar
# print(fibonachi(10))
