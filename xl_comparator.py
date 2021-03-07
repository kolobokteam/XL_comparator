# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:20:39 2021

@author: ashmanov
"""

# import pandas
import openpyxl
# from table_select import table_select
from tabulate import tabulate

filename1 = "1_й_Этап_Отделка_квартир,_МОП,_внутренние_инженерные_системы_от.xlsx"
filename2 = "1_й_Этап_Отделка_квартир,_МОП,_внутренние_инженерные_системы_от (2).xlsx"

file1 = openpyxl.load_workbook(filename1)
file2 = openpyxl.load_workbook(filename2)

sheets_file1 = [sheet.title for sheet in file1.worksheets]
sheets_file2 = [sheet.title for sheet in file2.worksheets]

# sheets_file1, sheets_file2 = table_select(filename1, filename2)
if sheets_file1 != sheets_file2:
    print("Листы в этих файлах, неодинаковые.\n")
    dict1 = {filename1 : [title for title in sheets_file1], filename2 : [title for title in sheets_file2]}
    print(tabulate(dict1, headers=[filename1[0:11]+"..."+filename1[-15:-5], filename2[0:11]+"..."+filename2[-15:-5]], tablefmt="pretty"))
    print("\nВам нужно выбрать, какие листы вы хотите сравнить.")
    while True:
        select = input("Лист из первого файла: ")
        if select.lower() in [sheet_file1.lower() for sheet_file1 in sheets_file1]:
            sheet1 = file1[select]
            file1.active = sheet1
            break
        else:
            print("Такого листа в файле нет. Попробуйте ещё")
    while True:
        select = input("Лист из второго файла: ")
        if select.lower() in [sheet_file2.lower() for sheet_file2 in sheets_file2]:
            sheet2 = file2[select]
            file2.active = sheet2
            break
        else:
            print("Такого листа в файле нет. Попробуйте ещё")
else:
    pass


for sheet1_row in sheet1.rows:
    pass
for sheet2_row in sheet2.rows:
    pass
if sheet1_row == sheet2_row:
    print("Строки равны")
else:
    print("Строки не одинаковые")
