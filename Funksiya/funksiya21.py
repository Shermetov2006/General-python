# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:26:35 2024

@author: фвьшт
"""
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f'talaba {ism.title()}ni baholang:')
    return baholar

talabalar=['azamat', 'jabohir' , 'jiha', 'umar']
baholar=bahola(talabalar[:])
print(baholar)
print(talabalar)
