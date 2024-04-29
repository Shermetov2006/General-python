# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:36:41 2024

@author: ПИРМУХАММАД
"""
import random as r 

def son_top(x=10):
    tasodifiy_son=r.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    tahminlar=0
    
    while True:
        tahminlar+=1
        tahmin=int(input(">>>"))
        if tasodifiy_son>tahmin:
            print(f"Men o'ylagan son <{tahmin}> dan kattaroq. Yana Harakat qilib ko'ring!")
        elif tasodifiy_son<tahmin:
            print(f"Men o'ylagan son <{tahmin}> dan kichikroq. Yana Harakat qilib ko'ring!")
        else:
            break
    print(f"Tabriklaymiz. Topdingiz! Siz buni <{tahminlar}> ta tahmin bilan topdingiz! \n")
    return tahminlar

def son_top_camp(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. MEN TOPAMAN! ")
    quyi=1
    yuqori=x
    tahminlar=0
    while True:
        tahminlar+=1
        if quyi != yuqori:
            tahmin=r.randint(quyi, yuqori)
        else:
            tahmin=quyi
        javob=input(f"\nSiz tanlagan raqam <{tahmin}>. To'g'ri bo'lsa(t), Kichik bo'lsa (-), Katta bo'lsa (+) yozing!".lower())
        if javob == '-':
            yuqori=tahmin - 1
        elif javob == '+':
            quyi=tahmin+1
        else:
            break
    print(f"Topdim!  Men buni <{tahminlar}> ta tahmin bilan topdim! \n")
    return tahminlar

def play(x=10):
    yana=True
    while yana:
        tahminlar_user=son_top(x)
        tahminlar_camp=son_top_camp(x)
        
        if tahminlar_camp<tahminlar_user:
            print("MEN YUTDIM!!!")
        elif tahminlar_camp>tahminlar_user:
            print("SIZ YUTDINGIZ!!!")
            print("\nO'ZI YUTQAZMOQCHIMASDIM-U MAYLI YUTAQOLSIN DEDIM!")
        else:
            print("DURRANG!!!")
        yana=int(input("\nYana o'ynashni hohlaysizmi?[son kiriting] HA(1)/YO'Q(0): "))
    print("O'YIN BATAMOM YAKUNLANDI")
    
    
print(play())
    