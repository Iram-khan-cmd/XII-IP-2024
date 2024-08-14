#Practical 1
#PROGRAM 1
'''
PROGRAM DEVELOPED BY: SHARON AMUS
TIME: 12:00PM
MENU DRIVEN PROGRAM DEMONSTRATING CREATION OF SERIES...
SERIES IS ONE-DIMENSIONAL
SERIES IS SIZE IMMUTABLE
SERIES IS VALUE IMMUTABLE'''

import pandas as pd
import numpy as np
def menu():
    print("**********SERIES CREATION FUNDAMENTALS**********")
    print("Press 1: Creation of Series from Scalar Values")
    print("Press 2: Creation of Series from Numpy n-d arrays")
    print("Press 3: Creation of Series from list using integers")
    print("Press 4: Creation of Series from list using Floating Point Numbers")
    print("Press 5: Creation of Series from List with Strings")
    print("Press 6: Creation of Series from Nested Lists")
    print("Press 7: Creation of Series from dictionary")
    print("Press 8: Creation of Series from Nested dictionary")
    print("Press 9: Creation of Series from List of Dictionaries")
    print("Press 10: Creation of Empty Series")
    print("Press 0 : Exit")
    print("*************************************************")
        
def scalar():
        print("Demonstrating the creation of series from Scalar Values ")
        s1=pd.Series(34,index=[1,2,3,4,5])
        print(s1)

def Numpy_nd_array():
        print("Demonstrating the creation of series from Numpy n-d arrays")
        arr= np.arange(10,40,2)
        s2=pd.Series(arr)
        print(s2)

def int_series():
        print("Demonstrating the creation of series from integer Values ")
        s3=pd.Series([23,13,89,34,80],index=[1,2,3,4,5])
        print(s3)


def float_series():
        print("Demonstrating the creation of series from Floating Point Numbers")
        s4=pd.Series([23.98,56.45,88,99,45],index=[1,2,3,4,5])
        print(s4)

def String_series():
        print("Demonstrating the creation of series from List with Strings")
        s5=pd.Series([23.98,56.45,88,99,45,'shubham','keerti'],index=[1,2,3,4,5,6,7])
        print(s5)

def nested_list_series():
        print("Demonstrating the creation of series from Nested Lists")
        s6=pd.Series([23.98,56.45,88,99,45,['shubham','keerti'],[22,45]],index=[1,2,3,4,5,6,7])
        print(s6)

def Dictionary_series():
        print("Demonstrating the creation of series from dictionary")
        s7=pd.Series({"Temperature":[23.98,56.45],"Pressure":[22,45,48]})
        print(s7)
def Nested_Dictionary_series():
        print("Demonstrating the creation of series from Nested dictionary")
        s8=pd.Series({"Marks":{"Nidhi":34,"Mahita":38},"age":{"Nidhi":17,"Mahita":19}})
        print(s8)

def lists_of_Dictionary_series():
        print("Demonstrating the creation of series from lists_of_dictionary")
        dict1={"Marks":38,"Name":"Jonathan"}
        dict2={"age":19,"Name":"Jonathan" }
        s9=pd.Series([dict1,dict2],index=["Marks_stud","Age_stud"])
        print(s9)
def Empty_series():
    s10=pd.Series(None)
    print(s10)
    
menu()
while True:
    ch=int(input("INPUT YOUR CHOICE: "))
    if ch==1:
        scalar()
    elif ch==2:
        Numpy_nd_array()
    elif ch==3:
        int_series()
    elif ch==4:
        float_series()
    elif ch==5:
        String_series()
    elif ch==6:
        nested_list_series()
    elif ch==7:
        Dictionary_series()
    elif ch==8:
        Nested_Dictionary_series()
    elif ch==9:
        lists_of_Dictionary_series()
    elif ch==10:
        Empty_series()
    else:
        ch==0
        break
