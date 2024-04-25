# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:11:14 2024

@author: фвьшт
"""

import random as r 
savol="\n(DASTURIMIZ O'ZBEK TILIDA')\n"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing yoki ENTER): "

while True:
    qiymat=input(savol)
    if qiymat.lower() == 'exit':
        print("DASTUR TO'XTADI")
        break
        
    
    else:
        m=(input("\nBIZNING O'YINDA QATNASHASIZMI:\n ha\yoq: "))

        if m.lower()=="ha" :
            
            c=int(input("O'yin 5000 so'm \n pul kiriting: "))
            if c>=5000:
                print("Rahmat. O'YINNI BOSHLASHINGIZ MUMKIN! ")
                
                b= int(input("son kiriting: "))
                a=r.randint(1, 5)
                if a==b:
                    print("SIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN.")
                else:
                    print(f"SIZ YUTQAZDINGIZ SIZ TALLAGAN RAQAM {b} \nTASODIFIY SON {a}")
                
            
                
            else:
                print("PULINGIZ KAM!")



        else:
            print("TASHRIFINGIZ UCHUN RAHMAT")


   
    
