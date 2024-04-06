# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:30:00 2024

@author: фвьшт
"""


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "#

# while True:
#    qiymat=input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)


#sonlar = list(range(1, 11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f'{son} ni kvadrati {son**2}')


#sonlar = list(range(1, 11))
#for son in sonlar:
#    if son == 5:
#        continue
#    print(f'{son} ni kvadrati {son**2}')


#son = 0
#while son<10:
#    son +=1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
        
#son = 1
#while son>0:
#    son +=1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
        
 
'''Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
 Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating'''
 
 
savol="yaxshi ko'rgan kitoblarini kiriting: "
savol += "\nkitoblarni kiritgach 'stop' buyrug'ini bering."

while True:
    qiymat = input(savol)
    if qiymat =='stop':
        break
    else:
        print(savol)
        
a='dastur tugadi'
print(f"{a.upper()}")