# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:48:33 2020

@author: Mohamed M. Omran
"""

import random

def draw_dice_face(number):
    if number == 1:
        print("---------")
        print("|       |")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("|       |")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("|       |")
        print("---------")
    elif number == 3:
        print("---------")
        print("|       |")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("|       |")
        print("---------")
    elif number == 4:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")
    elif number == 5:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("|       |")
        print("---------")
    else:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("|       |")
        print("---------")
    return

dice_faces = [1,2,3,4,5,6]

answer = "y"

while answer == "y":
    x = random.randint(1,6)
    draw_dice_face(x)
    print(x)
    y = random.randint(1,6)
    print(y)
    draw_dice_face(y)
    
    answer = input("\nRoll again?  (y / n)  ")
