# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:24:52 2021

@author: admOS
"""

def summa(maximum, num1, num2):
    nums = [i for i in range(1, maximum) if (i%num1 == 0 or i%num2 == 0)]
    return sum(nums)

def task2(maximum):
    fibo = [1, 2]
    i = sum(fibo)
    while i < maximum:
        i = fibo[-1] + fibo[-2]
        fibo.append(i)
    row = []
    for index, num in enumerate(fibo, 1):
        if index%2 == 0:
            row.append(num)
    return sum(row)

if __name__ == "__main__":
    # print(summa(1000, 3, 5))
    print(task2(4_000_000))