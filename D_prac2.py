#Practical2
'''
OPERATIONS ON DATAFRAME
1.ADDING A ROW
2.ADDING A COLUMN
3.DELETING ROW
4.DELETING COLUMN
5.RENAMING ROW LABELS
6. RENAMING COLUMN LABELS

'''
import pandas as pd
#Creation of DataFrame
Data = {'Coach Name':['Ashika','Farha','Shayan','Akshara','Kunal','Tarun','Shailya','Samad','Tarana','Charlie'],
        'Age':[35,34,33,36,39,37,41,37,31,30],
        'Sports':['Karate','Karate','Squash','Basketball','Swimming','Swimming','Squash','Karate','Swimming','Basketball'],
        'Date of app':['27/03/1996','20/01/1998','19/02\1998','01/01/1998','12/01/1998','24/02/1998','22/02/1998','22/02/1998','13/01/1998','19/02/1998'],
        'Pay':[1000,1200,2000,1500,750,800,2200,1100,900,1700]}
D=pd.DataFrame(Data,index=[1,2,3,4,5,6,7,8,9,10])
print(D)
def menu():
        print("1.Adding a row:")
        print("2.Adding a column:")
        print("3.Deleting a row:")
        print("4.Deleting a column:")
        print("5.Renaming row labels:")
        print("6.Renaming column labels:")
        print("7.Modifying the data :")
        print("8.Checking any record in the data:")
        print("9.Accessing any record from the data:")
        print("10.Exit:")
def Adding_Row():
        print("Adding a row: ")
        D.loc[11]=['Rina','33','Badminton','25/5/1998',1500]
        print(D)
def Adding_column():
        print("Adding column:")
        D['Gender']=['F','F','M','F','M','M','F','M','F','M','F']
        print(D)
def Deleting_Row():
        print("Deleting a row:")
        D.drop(6,axis=0,inplace=True)
        print(D)
def Deleting_column():
        print("Deleting a column:")
        D.drop('Gender',axis=1,inplace=True)
        print(D)
def Renaming_Row_Label():
        print("Renaming row labels:")
        D.rename({1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'},axis='index',inplace=True)
        print(D)
def Renaming_column_Label():
        print("Renaming column labels:")
        D.rename({'Coach Name':'S1','Age':'S2','Sports':'S3','Date Of App':'S4','Age':'S5'},axis='columns',inplace=True)
        print(D)

def Modifying_Data():
        print("Modifying Data:")
        D.at[1,'Age']=37
        print(D)
        
def Checking_Record():
        print("Checking record in data:")
        print('Ashika' in D)

def Accessing_Data():
        print("Accessing any record from the data:")
        print(D.loc[1,'Coach Name'])

def Exit():
        exit(0)
    

menu()
while True:
    ch=int(input("INPUT YOUR CHOICE: "))
    if ch==1:
        Adding_Row()
    elif ch==2:
        Adding_column()
    elif ch==3:
        Deleting_Row()
    elif ch==4:
         Deleting_column()
    elif ch==5:
        Renaming_Row_Label()
    elif ch==6:
        Renaming_column_Label()
    elif ch==7:
        Modifying_Data()
    elif ch==8:
        Checking_Record()
    elif ch==9:
        Accessing_Data()

    elif ch==10:
        Exit()
            
        
        
#accessing data function does not work until you press 2, cuz when u press 2 it will show the gender column and then the accessing funtion find all the columns then it will run perfactly.
        
        
        

        
       
       

