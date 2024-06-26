# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 07:47:32 2024

@author: ПИРМУХАММАД
"""

import turtle as tur 
import colorsys as cs
tur.setup(128,102)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
for j in range(50):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15, j/25, 1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()        