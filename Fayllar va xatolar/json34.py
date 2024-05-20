# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:27:15 2024

@author: фвьшт
"""

import json 

# a= 10
# a_json= json.dumps(a )

# sonlar=(12,245,245,245)
# sonlar_json=json.dumps(sonlar)

bemor={
        "ism":"anvar",
        "oila":True,
        "dorilar": [
            {"nomi":"anlgin","narhi":1000},
            {"nomi":"panadol","miqdori":2000}
            ]
        }
bemor_json=json.dumps(bemor, indent=4)
print(bemor_json)

# with open("bemor.json", "w") as bemor:
#     json.dump(bemor, bemor)
