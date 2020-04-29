import os
import sys
import functions as f
import shutil
import pathlib
import csv_f
import zlib
import Flags
from os import listdir
from os.path import isfile, join
#import pandas
#import xlrd
import Description as d
import Weapons


input = csv_f.make_list("input1.csv")
#input = csv_f.load_xlsx("input.xlsx")


pack_name = 'Weapon_pack004'
Weapons.newWeaponPack(input, pack_name)

