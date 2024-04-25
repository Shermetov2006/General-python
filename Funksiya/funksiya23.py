# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:11:14 2024

@author: фвьшт
"""

import random as r 
savol="\n(DASTURIMIZ O'ZBEK TILIDA)\n"
savol+="(HAR BIR MATNNI DIQQAT BILAN O'QING ILTIMOS!)\n"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing yoki ENTER): "

while True:
    qiymat=input(savol)
    if qiymat.lower() == 'exit':
        print("DASTUR TO'XTADI")
        break
        
    
    else:
        m=(input("\nO'YIN NARXI 5000 SO'M! \nBIZNING O'YINDA QATNASHASIZMI:\n ha\yoq: "))

        if m.lower()=="ha" :
            
            
            
            while True:
                c=float(input("\nBIZNING O'YINIMIZDA SIZ QANDAYDIR SON TANLAYSIZ RANDOM HAM QANDAYDIR SON TANLAYDI "
                       "\nAGAR IKKALA SON YOKI RAQAM TENG BO'LSA SIZ YUTASIZ. AKS HOLDA YUTQAZASIZ!\n" 
                         "\n SIZ 5000 SO'MDAN QANCH KO'PROQ PUL KIRITSANGIZ, BIZ O'SHA PULNI BOLALAR UYIGA BERAMIZ.\n \nO'YIN NARXI 5000 so'm \n pul kiriting: "))
                
                if c==5000:
                    print("\nRahmat. O'YINNI BOSHLASHINGIZ MUMKIN! ")
                    break
                    
                    b= int(input("son kiriting: "))
                    a=r.randint(1,2)
                    if a==b:
                        print("\nSIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                            f"RANDOM TANLAGAN RAQAM {a}")
                    
                                    
                elif c>5000:
                    print(f"\nRAHMAT. SIZ {c-5000} so'm ko'p pul berdingiz. BIZ BU PULNI SIZNING NOMINGIZDAN BOLALAR UYIGA BERAMIZ."
                          f"\nSIZ UYALMASDAN {c-5000} SO'M BERDIM DEB HIJOLAT BO'LMANG. SAVOBNING KATTA KICHIKI BO'LMAYDI.")
                    break
                
                b= int(input("son kiriting: "))
                a=r.randint(1,2)
                if a==b:
                    print("\nSIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                            f"RANDOM TANLAGAN RAQAM {a}")
                    
                else:
                    print("PULINGIZ KAM!")
            
            
            
            
            
            
            
            # c=float(input("\nBIZNING O'YINIMIZDA SIZ QANDAYDIR SON TANLAYSIZ RANDOM HAM QANDAYDIR SON TANLAYDI "
            #             "\nAGAR IKKALA SON YOKI RAQAM TENG BO'LSA SIZ YUTASIZ. AKS HOLDA YUTQAZASIZ!\n" 
            #            "\n SIZ 5000 SO'MDAN QANCH KO'PROQ PUL KIRITSANGIZ, BIZ O'SHA PULNI BOLALAR UYIGA BERAMIZ.\n \nO'YIN NARXI 5000 so'm \n pul kiriting: "))
            
            # # while True:
                # if c==5000:
                #     print("\nRahmat. O'YINNI BOSHLASHINGIZ MUMKIN! ")
                #     break
                    
                #     b= int(input("son kiriting: "))
                #     a=r.randint(1,2)
                #     if a==b:
                #         print("\nSIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                #             f"RANDOM TANLAGAN RAQAM {a}")
                    
            #     elif c>5000:
                    # print(f"\nRAHMAT. SIZ {c-5000} so'm ko'p pul berdingiz. BIZ BU PULNI SIZNING NOMINGIZDAN BOLALAR UYIGA BERAMIZ."
                    #       f"\nSIZ UYALMASDAN {c-5000} SO'M BERDIM DEB HIJOLAT BO'LMANG. SAVOBNING KATTA KICHIKI BO'LMAYDI.")
                    # break
                
                    # b= int(input("son kiriting: "))
                    # a=r.randint(1,2)
                    # if a==b:
                    #     print("\nSIZ YUTDINGIZ. [YOU WIN] \nSOVG'ANGIZNI BIZNING FILIALLARDAN OLIB KETISHINGIZ MUMKIN."
                    #         f"RANDOM TANLAGAN RAQAM {a}")
            #         else:
            #             print(f"SIZ YUTQAZDINGIZ SIZ TALLAGAN RAQAM {b} \nTASODIFIY SON {a}")
                    
                
            #     else:
            #         print("PULINGIZ KAM!")

        
        
                
                
                
                
                



        else:
            print("TASHRIFINGIZ UCHUN RAHMAT")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # while True:
            #     a=int(input("pul kiriting: "))
            #     if a==5000 :
            #         print("RAHMAT!")
            #         break

            #     elif a>5000:
            #         print(f"RAHMAT. SIZ {a-5000} so'm ko'p pul berdingiz. BIZ BU PULNI SIZNING NOMINGIZDAN BOLALAR UYIGA BERAMIZ."
            #               f"\nSIZ UYALMASDAN {a-5000} SO'M BERDIM DEB HIJOLAT BO'LMANG. SAVOBNING KATTA KICHIKI BO'LMAYDI.")
            #         break
                    
            #     else:
            #         print("yo'q")


   
    
