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


sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        break
    print(f'{son} ni kvadrati {son**2}')


sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        continue
    print(f'{son} ni kvadrati {son**2}')
