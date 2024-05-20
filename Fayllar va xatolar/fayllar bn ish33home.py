# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:56:39 2024

@author: фвьшт
"""
import pickle
with open("python.txt") as file:
    pi= file.read()

bdata="11142007"
print(bdata in pi)

pi=float(pi)

with open("of", "wb"):
    pickle.write(pi, file)

    