#4
import pandas as pd
import numpy as np
my_dict = {}
my_dict1 = {}
print('MATHEMATICAL OPERATONS ON TWO SERIES OF DICTIONARIES\n')
num_pairs = int(input('Enter the number of key-value paris to enter for the first dictionary:'))
for i in range(num_pairs) :
    key = input('Enter key :')
    value = int(input('Enter value for key :'))
    my_dict[key] = value
print('\nYour Dictionary :')
print(my_dict)
dic = pd.Series(my_dict)
print('Series of dictionary :')
print(dic)
print('\nVector operations :\n')
print('1. Vectorized Addition ')
print('2. Vectorized Subtraction ')
print('3. Vectorized Multiplication ')
print('4. Vectorized Exponentiation ')
print('5. Vectorized Division ')
print('6. Vectorized Comparision')
print('7. Exit\n')
while True :
    ch = int(input('Enter your choice : '))
    if ch == 1 :
        add = int(input('Enter the number to be added in each item of the series : '))
        ad = dic + add
        print(ad)
    elif ch == 2 :
        sub = int(input('Enter the number to be subtracted from each item of the series : '))
        su = dic - sub
        print(su)
    elif ch == 3 :
        mul = int(input('Enter the number to be multipied with each item of the series : '))
        mu = dic * mul
        print(mu)
    elif ch == 4 :
        exp = int(input('Enter the exponent : '))
        ex = dic ** exp
        print(ex)
    elif ch == 5 :
        div = int(input('Enter the divisor : '))
        di = dic / div
        print(di)
    elif ch == 6 :
        TF = int(input('Enter the number you think is greater than each item of the series : '))
        FT = TF > dic
        print(FT)
    elif ch == 7 :
        break
