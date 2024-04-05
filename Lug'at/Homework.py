# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:06:15 2024

@author: фвьшт
"""

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asar':'Aziz'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asar':'Muqaddas'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asar':'Ozbegim'
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asar':'Xamsa'
           }

shaxslar=[buxoriy, qodiriy, vohidov, navoiy]

for shahs in shaxslar:
    ism=shahs['ism']
    tyil=shahs['tyil']
    vyil=shahs['vyil']
    tjoy=shahs['tjoy']
    asar=shahs['asar']
    print(f'{ism} {tyil}da {tjoy}da tugilgan.'
          f'{ism} {vyil-tyil} da vafot etgan'
          f'{ism} "{asar.upper()}" asarini yozgan')
    
    
    
    kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
    
    
for ism,kinolar in kinolar.items():
    print(f"\n{ism.title()} yoqtiradigan kino: ")
    for kino in kinolar:
        print(kino)
        
        
        
        
        
        
        
        
        
        
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
                }


#for davlat, info in davlatlar.items():
#    if davlat.lower()=='aqsh':
#        davlat = davlat.upper()
#    else:
#        davlat = davlat.capitalize()
#    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#          f"\nHududi: {info['maydon']} kv.km"
#          f"\nAholisi: {info['aholi']}"
#          f"\nPul birligi: {info['pul birligi']}")
    #2-bo'lim

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")

    
    
    
    