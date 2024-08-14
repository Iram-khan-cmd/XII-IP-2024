'''#Create a menu driven program in python to create two series .arithematic operation on these series.
import pandas as pd
def menu():
    print('\nMathematical operations :\n')
    print('1. Addition of series')
    print('2. Subtraction of series')
    print('3. Multiplication of series')
    print('4. Division of series')
    print('5. Enter any number to exit the program\n')

def series_creation():
    s1 = pd.Series([12,34,56,78,90,13])
    print("series 1 is:")
    print(s1)
    #series2
    s2= pd.Series([30,67,89,12,59,51])
    print("Series  2 is:")
    print(s2)

def choice():
    series_creation()
    ch =int(input('Enter your choice :'))
    if ch==1:
        Addition= s1+s2 
        print(Addition)
    elif ch==2:
        Subtraction= s1-s2 
        print(Subtraction)
    elif ch==3:
        Multiplication= s1*s2 
        print(Multiplication)
    elif ch==4:
        Division= s1/s2 
        print(Division)
    else :
        ch==5
        exit(0)

def main():
    series_creation()
    menu()
    choice()
main()'''



import pandas as pd

# Define series globally
s1 = pd.Series([12, 34, 56, 78, 90, 13])
s2 = pd.Series([30, 67, 89, 12, 59, 51])

def menu():
    print('\nMathematical operations :\n')
    print('1. Addition of series')
    print('2. Subtraction of series')
    print('3. Multiplication of series')
    print('4. Division of series')
    print('5. Exit the program\n')

def series_creation():
    print("Series 1 is:")
    print(s1)
    print("\nSeries 2 is:")
    print(s2)

def choice():
    ch = int(input('Enter your choice: '))
    if ch == 1:
        Addition = s1 + s2
        print("\nAddition of series:\n", Addition)
    elif ch == 2:
        Subtraction = s1 - s2
        print("\nSubtraction of series:\n", Subtraction)
    elif ch == 3:
        Multiplication = s1 * s2
        print("\nMultiplication of series:\n", Multiplication)
    elif ch == 4:
        Division = s1 / s2
        print("\nDivision of series:\n", Division)
    elif ch == 5:
        print("\nExiting the program.")
        exit(0)
    else:
        print("\nInvalid choice. Please enter a valid option.")

def main():
    series_creation()
    while True:
        menu()
        choice()


main()


