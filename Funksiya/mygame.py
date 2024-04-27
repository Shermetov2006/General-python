# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:10:28 2024

@author: фвьшт
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:44:26 2024

@author: фвьшт
"""

import random as r 
savol="\n>(DASTURIMIZ O'ZBEK TILIDA)\n"
savol+=">>(HAR BIR MATNNI DIQQAT BILAN O'QING ILTIMOS!)\n"
savol += ">>>(dasturni to'xtatish uchun 'EXIT' deb yozing yoki boshlash uchun ENTER): "

while True:
    qiymat=input(savol)
    if qiymat.lower() == 'exit':
        print("DASTUR TO'XTADI")
        break
        
    
    else:
        m=(input("\nO'YIN NARXI 5000 SO'M! \nBIZNING O'YINDA QATNASHASIZMI:\n ha\yoq: "))

        if m.lower()=="ha" :
            c=float(input("\nBIZNING O'YINIMIZDA SIZ QANDAYDIR SON TANLAYSIZ RANDOM HAM QANDAYDIR SON TANLAYDI "
                        "\nAGAR IKKALA SON YOKI RAQAM TENG BO'LSA SIZ YUTASIZ. AKS HOLDA YUTQAZASIZ!\n" 
                        "\n SIZ 5000 SO'MDAN QANCH KO'PROQ PUL KIRITSANGIZ, BIZ O'SHA PULNI BOLALAR UYIGA BERAMIZ.\n \nO'YIN NARXI 5000 so'm \n pul kiriting: "))
            
            if c==5000:
                    print("\n>Rahmat. O'YINNI BOSHLASHINGIZ MUMKIN! ")
                    
                    
                    b= int(input("SON yoki RAQAM kiriting: \n"))
                    a=r.randint(1, 9)
                    if a==b:
                        print("\n>>>SIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                                      f"RANDOM TANLAGAN RAQAM {a}")
                        if b>10:
                            print(f">>>SIZ YUTQAZDINGIZ SIZ TALLAGAN SON {b} \nTASODIFIY RAQAM {a}")
                            
                    else:
                         print(f"\n>>>SIZ YUTQAZDINGIZ SIZ TALLAGAN SON {b} \nTASODIFIY RAQAM {a}")
            elif c>5000:
                if c<10000:
                    print(f"\nRAHMAT. SIZ {c-5000} so'm ko'p pul berdingiz. BIZ BU PULNI SIZNING NOMINGIZDAN BOLALAR UYIGA BERAMIZ."
                          f"\nSIZ UYALMASDAN {c-5000} SO'M BERDIM DEB HIJOLAT BO'LMANG. SAVOBNING KATTA KICHIKI BO'LMAYDI.")
                    
                    b= int(input("SON yoki RAQAM kiriting: \n"))
                    a=r.randint(1,9)
                    if a==b:
                        print("\n>>>SIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                            f"RANDOM TANLAGAN RAQAM {a}")
                    
                    else:
                         print(f"\n>>>SIZ YUTQAZDINGIZ SIZ TALLAGAN SON {b} \nTASODIFIY RAQAM {a}")
                else:
                    print(f"\nRAHMAT. SIZ {c-5000} so'm ko'p pul berdingiz. BIZ BU PULNI SIZNING NOMINGIZDAN BOLALAR UYIGA BERAMIZ."
                          f"\n SAVOBNING KATTA KICHIKI BO'LMAYDI.")
                    
                
                    b= int(input("SON yoki RAQAM kiriting: \n"))
                    a=r.randint(1,9)
                    if a==b:
                        print("\nSIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                            f"RANDOM TANLAGAN RAQAM {a}")
                    else:
                         print(f">>>SIZ YUTQAZDINGIZ SIZ TALLAGAN SON {b} \nTASODIFIY RAQAM {a}")
            else:
                    print("PULINGIZ KAM!")
        else:
            print("TASHRIFINGIZ UCHUN RAHMAT")