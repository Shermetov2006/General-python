# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:15:52 2024

@author: ПИРМУХАММАД
#randint= tasodifiy sonlarni aniqlaydi
choice = listdan tanlaydi tasodifiy
shuffle = [place replyce] JOYLAEINI YANI ORNINI ALMASHTIRADI
"""
import random as r 


# import homework21 as h 
# from homework21 import katta_harf
# from homework21 import katta_harf as kh
# from homework21 import * #tavsiya qilinmaydi.

# import math
# a=400
# print(math.sqrt(a))
# print(math.pow(5, 3))
# print(math.pi)
# print(math.log2(1024))
# print(math.log10(100000))


# son = r.randint(1,100)
# print(son)

# ismlar=['silam','anbar','jahon','uamr']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# s=list(range(2,55,5))
# print(s)
# print(r.choice(s))

m=list(range(11))
print(m)
r.shuffle(m)
print(m)

