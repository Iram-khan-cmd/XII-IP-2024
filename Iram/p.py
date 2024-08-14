import pandas as pd
Data = {'Coach Name':['Ashika','Farha','Shayan','Akshara','Kunal','Tarun','Shailya','Samad','Tarana','Charlie'],'Age':[35,34,33,36,39,37,41,37,31,30],'Sports':['Karate','Karate','Squash','Basketball','Swimming','Swimming','Squash','Karate','Swimming','Basketball'],'Date of app':['27/03/1996','20/01/1998','19/02\1998','01/01/1998','12/01/1998','24/02/1998','22/02/1998','22/02/1998','13/01/1998','19/02/1998'],'Pay':[1000,1200,2000,1500,750,800,2200,1100,900,1700]}
D = pd.DataFrame(Data,index=[1,2,3,4,5,6,7,8,9,10])
print(D)
print("Adding a row: ")
D.loc[11]=['Rina','33','Badminton','25/5/1998',1500]
print(D)
D['Gender']=['F','F','M','F','M','M','F','M','F','M','F']
print(D)
print("Deleting a row:")
D.drop(6,axis=0,inplace=True)
print(D)
print("Deleting a column:")
D.drop('Gender',axis=1,inplace=True)
print(D)
D = D.rename({''})



       
