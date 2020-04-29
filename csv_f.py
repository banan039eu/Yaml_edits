import os
import sys
import csv
#import xlrd

def load_csv(file):
    csvfile = open(file, newline='')
    data = csv.reader(csvfile, delimiter=';', quotechar='|')
    return data

def load_xlsx(file):
    book = xlrd.open_workbook(file)
    sheet = book.sheet_by_index(0)
    list = []
    for k in range(0, sheet.nrows):
        tmp = []
        for j in range(0, sheet.ncols):
            tmp.append(str(sheet.row_values(k)[j]))
        list.append(tmp)
    return list
def make_list(file):
    data = load_csv(file)
    input = []
    for row in data:
        input.append(row)
    return input