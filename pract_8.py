#Practical 8
#Consider following Data. Create a Series and answer questions that follow
import pandas as pd
print("Sales data:")
Sales_Series = pd.Series([25000,34000,31000,20000,27000,39000,22000,41000],index = ['January','February','March','April','May','June','july','August'])
print(Sales_Series)
#1. How do you access the sales data for the month of 'March' from the `sales` Series?
print(" Sales data for the month of 'March':")
print(Sales_Series['March'])
#2.Write a code snippet to extract sales data from 'February' to 'June' (inclusive) from the `sales` Series using slicing.
print("Sales data from February to June:")
print(Sales_Series['February':'June'])

#3.Filter and display the sales data for months where sales exceeded $30,000 in the `sales` Series.
print("Sales data where sales exceeds $30000:")
print(Sales_Series[Sales_Series>30000])
#4.Check if the month 'August' exists in the index of the `sales` Series.
print('August' in Sales_Series )
#5.Create a new Series containing sales data for the months 'January', 'March', and 'May' from the `sales` Series, using list of labels.
New = Sales_Series['January':'May':2]
New_s = pd.Series(New)
print(New_s)

#6. Retrieve the sales data for the third month in the `sales` Series using integer- location based indexing.
print("Sales data for third month:")
print(Sales_Series.iloc[2])
#7. How to slice the `sales` Series to access all elements except the last two months.
print("Acessing all elements except the last two:")
print(Sales_Series['January':'June'])
