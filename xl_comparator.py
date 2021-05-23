# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:20:39 2021

@author: ashmanov
"""

# import pandas
import openpyxl
from itertools import zip_longest
# from table_select import table_select
from tabulate import tabulate


filename1 = "1_й_Этап_Отделка_квартир,_МОП,_внутренние_инженерные_системы_от.xlsx"
filename2 = "1_й_Этап_Отделка_квартир,_МОП,_внутренние_инженерные_системы_от (2).xlsx"
filename1 = "file1.xlsx"
filename2 = "file2.xlsx"

file1 = openpyxl.load_workbook(filename1)
file2 = openpyxl.load_workbook(filename2)
result_file = openpyxl.Workbook()
result_file.active.title = "Результат обработки"
result_file.active.sheet_properties.tabColor = "FF0000"

sheets_file1 = [sheet.title for sheet in file1.worksheets]
sheets_file2 = [sheet.title for sheet in file2.worksheets]

# sheets_file1, sheets_file2 = table_select(filename1, filename2)
if any([sheets_file1 != sheets_file2, all([len(sheets_file1) == len(sheets_file2), len(sheets_file1) > 1, len(sheets_file2) > 1])]):
    dict1 = {filename1 : [title for title in sheets_file1], filename2 : [title for title in sheets_file2]}
    print(tabulate(dict1, headers=[filename1[0:11]+"..."+filename1[-15:-5], filename2[0:11]+"..."+filename2[-15:-5]], tablefmt="pretty"))
    print("\nВам нужно выбрать, какие листы вы хотите сравнить.")
    while True:
        select = input("Лист из первого файла: ")
        if select in [sheet_file1 for sheet_file1 in sheets_file1]:
            sheet1 = file1[select]
            file1.active = sheet1
            break
        else:
            print("Такого листа в файле нет. Попробуйте ещё")
    while True:
        select = input("Лист из второго файла: ")
        if select in [sheet_file2 for sheet_file2 in sheets_file2]:
            sheet2 = file2[select]
            file2.active = sheet2
            break
        else:
            print("Такого листа в файле нет. Попробуйте ещё")
else:
            sheet1 = file1.active
            sheet2 = file2.active


<<<<<<< HEAD
for sheet1_row, sheet2_row in zip_longest(sheet1.rows, sheet2.rows):
    for cell_sheet1_row, cell_sheet2_row in zip_longest(sheet1_row, sheet2_row):
        with open("result.txt", "a") as file:
            try:
                if cell_sheet1_row.value == cell_sheet2_row.value:
                    pass
                else:
                    print("Not equal")
            except:
                pass
=======
for sheet1_row, sheet2_row in zip(sheet1.rows, sheet2.rows):
    for cell_sheet1_row, cell_sheet2_row in zip(sheet1_row, sheet2_row):
        if cell_sheet1_row.value == cell_sheet2_row.value:
            print("ячейки равны", cell_sheet1_row)
        else:
            print("ячейки не одинаковые", cell_sheet1_row)

>>>>>>> 66e1128b802c4d611415404ea97358d987ad7cec
