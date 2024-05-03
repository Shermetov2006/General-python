# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:08:11 2024

@author: фвьшт
"""

from translate import to_cyrillic, to_latin

matn=input("Matn Kiriting: ")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))