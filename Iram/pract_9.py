#practical9
# Create a Series from table given below. Apply various Series attributes to it and perform Series based analysis.
import pandas as pd
print("Series:")
series = pd .Series([22,33,78,45,90],index=['shanaya','Fatima','Rishi','Dev','Prajakat'])
print(series)

#Data type of the Series
print("\nData type of the Series:")
print(series.dtype)
 #Index of the Series
print("\nIndex of the Series:")
print(series.index)
#Values in the Series
print("\nValues in the Series:")
print(series.values)
#Shape of the Series
print("\nShape of the Series:")
print(series.shape)
 #Summary statistics
print("\nSummary statistics:")
print(series.describe())
 #Accessing individual elements
print("\nElement at index 'c':")
print(series['Rishi'])
 #Slicing the Series
print("\nSlicing the Series from index 'b' to 'd':")
print(series['Fatima':'Dev'])
