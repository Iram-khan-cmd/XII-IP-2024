#Program7
# Create a program in python to create Series objects named sales as shown below.
import pandas as pd
Series_sales = pd.Series([80000,50000,65000,70000,67000,77000,92000,81270,94560],index=['Alice','Bob','Charlie','David','Eva','Frank','Grace','Hannah','Ruth'])
print(Series_sales)
#1.#Display the sales of 'Charlie'.
print("Sales of charlie:")
Series_sales = Series_sales['Charlie']
print(Series_sales)
#2.#Find the average sales.
print("Average sales:")
print(Series_sales.mean())
#3.#Add 5000 to each salesperson's sales.
print("Adding 5000 to each salesperson's sales:")
print(Series_sales + 5000)
#4.#Find the highest and lowest sales in the Series.
print("Highest sales in the series are:")
print(Series_sales.max())
print("Lowest sales in the series are:")
print(Series_sales.min())
#5.#Display the names of the salespeople who sold more than 30000
print(":")
print(Series_sales[Series_sales<30000])
#6. Change the sales of 'Eva' to 28000.
print("sales of Eva:")
Series_sales[4] = 28000
print("updated sales of eva:",Series_sales)
#7.Create a new Series by dropping the sales of 'David'.
print("New Series:")
New_series = Series_sales.drop(['David'])
print(New_series)





