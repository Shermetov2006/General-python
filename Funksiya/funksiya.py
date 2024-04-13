# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:55:31 2024

@author: pirmuhammad
"""

#def salom_ber():
#    """salom beruvchi buyruq"""
#    print("assalomu aleykum")
#salom_ber()

#def salom__ber(ism):
#    """ismga salom beruvchi buyruq"""
#    print(f"assalomu aleykum {ism}")
#salom__ber("olim")
#salom__ber("usmon")

#def yoshni_top(ism,t_yil):
#   """bu yoshni hisoblaydi"""
#   print(f"{ism} {2024-t_yil} yoshda")
#yoshni_top(t_yil=1981,ism="qudrat")

#def t_yil(ism,yosh):
#    """bu tug'ilgan yilni hisoblaydi"""
#    print(f"{ism} {2024-yosh}-da tu'ilgan")
#t_yil("qudrat",43)
#t_yil(ism="qudrat", yosh=43)


#def yosh_hisoblash(tugilgan_yil, hozirgi_vaqt=2024):
#    """yoshni hisoblash ni yangi usulli"""
#    print(f"{hozirgi_vaqt-tugilgan_yil}")
#yosh_hisoblash(2005)

# -*- coding: utf-8 -*-


#3)#Foydalanuvchidan son olib, son juft yoki toqligini konsolga
# vchiqaruvchi funksiya yozing.

#def j_or_t(son):
#    if (son)%2!=0:
#        print(f"{son}  toq")
#    else:
#        print(f"{son} juft")
        
#j_or_t(5)
#j_or_t(10)



#4)#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga
# chiqaruvchifunksiya yozing. Agarsonlar teng bo'lsa "Sonlarteng"deganxabarnichiqaring.

#def katta_kichik(son,son2):
#    if son>son2:
#        print(f"{son}>{son2}")
#    elif son==son2:
#        print(f"{son}={son2}")
#    else:
#        print(f"{son}<{son2}")
#        
#katta_kichik(5,5 )


#5)#Foydalanuvchidan x va y sonlarini olib, ni konsolga
# chiqaruvchi funksiya yozing.
#Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

#def son(x,y=2):
#    print(x,y)
#son(5)
 

#6)#Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
# sonlarga qoldiqsiz bolinishini tekshiruvchi funksiya yozing. Natijalarni
# konsolga chiqaring.  

#def devide(son):
#    for i in range(2,11):
#        if not son%i:
#            print(f"{son} {i}ga qoldiqsiz bo'linadi")
#devide(8)