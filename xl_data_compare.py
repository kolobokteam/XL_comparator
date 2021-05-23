# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:24:18 2021

@author: ashmanov
"""

import openpyxl

def table_select(filename1, filename2):
    """
    

    Parameters
    ----------
    filename1 : string
        Первый файл для сравнения.
    filename2 : string
        Второй файл для сравнения.

    Returns
    -------
    sheets_file1 : list of string
        Список названий листов в книге1 (первом excel-файле).
    sheets_file2 : list of string
        Список названий листов в книге2 (втором excel-файле).

    """
    file1 = openpyxl.load_workbook(filename1)
    file2 = openpyxl.load_workbook(filename2)
    
    sheets_file1 = [sheet.title for sheet in file1.worksheets]
    sheets_file2 = [sheet.title for sheet in file2.worksheets]
    
    return sheets_file1, sheets_file2