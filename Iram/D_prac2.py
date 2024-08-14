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
Data = {'Coach Name':['Ashika','Farha','Shayan','Akshara','Kunal','Tarun','Shailya','Samad','Tarana','Charlie'],'Age':[35,34,33,36,39,37,41,37,31,30],'Sports':['Karate','Karate','Squash','Basketball','Swimming','Swimming','Squash','Karate','Swimming','Basketball'],'Date of app':['27/03/1996','20/01/1998','19/02\1998','01/01/1998','12/01/1998','24/02/1998','22/02/1998','22/02/1998','13/01/1998','19/02/1998'],'Pay':[1000,1200,2000,1500,750,800,2200,1100,900,1700]}
D = pd.DataFrame(Data,index=[1,2,3,4,5,6,7,8,9,10])
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
def Renaming_Row_Labels():
        print("Renaming row labels:")
        
        

        
       
       

