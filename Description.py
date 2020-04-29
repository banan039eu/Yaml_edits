'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import os
import sys


def dropLastChar(str):
    return str[:(len(str) - 1)]


def getLastChar(str):
    return str[(len(str) - 1):]


def calcOffset(size):
    if size <= 0:
        return 0
    else:
        return size


def dropFirstSpace(str):
    if str[0] == " ":
        return str[1:]
    else:
        return str


def createDesc(desc, line_size):
    lines = ['', '', '', '']
    words = desc.split(' ')
    i = 0
    for word in words:
        if (len(lines[i]) > line_size):
            lines[i] += "\\n"
            i += 1
        if (i > 3):
            break
        lines[i] += word + " "
    desc = ""
    for line in lines:
        desc += line
    desc = desc.replace(" \\n", "\\n")
    return desc

def peekDesc(desc):
    print(desc.replace("\\n", "\n"))

# desc = "The Master Sword was originally crafted by the goddess Hylia as the Goddess Sword, and was later forged into the Master Sword by the Goddess's chosen hero and its spirit, Fi, who bathed it in the three Sacred Flames located across the land that would become the Kingdom of Hyrule. Din's Flame in particular imbued the sword with the Power to Repel Evil, a power augmented after the Sword received the blessing of Zelda, which transformed the blade into the True Master Sword. It is usually the only Sword that can defeat Ganon in the games it appears in"
# line_size = 40
# print("\"" + createDesc(desc, line_size).replace("\\n", "\n") + "\"\n")
# peekDesc(createDesc(desc, line_size))
# print("\"" + desc + "\"\n")