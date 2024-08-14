#5
#consider the two series series1 and series2 .print the attributes of both these objects in areort from as shown below.
#Creation of series
import pandas as pd
sr1 = pd.Series([12,11,56,78,89])
print("Series1 is:")
print(sr1)
sr2 = pd.Series([33,66,80,72,10])
print("Series2 is:")
print(sr2)
#Statements here to create object s11 and s12 from previous examples
print("Attribute name \t\t\t object sr1 \t object sr2")
print("-----------------------------------------------------------")
print("Data type(.dtype)       :\t",sr1.dtype,'\t\t',sr2.dtype)
print("Shape   (.shape)        :\t",sr1.shape,'\t\t',sr2.shape)
print("No. of bytes(.nbytes)   :\t",sr1.nbytes,'\t\t',sr2.nbytes)
print("No. of dimensions(.ndim):\t",sr1.ndim,'\t\t',sr2.ndim)
print("Item size(.itemsize)    :\t",sr1.size,'\t\t',sr2.size)
print("Has NaNs?(.hasnans)     :\t",sr1.hasnans,'\t\t',sr2.hasnans)
print("Empty?(.empty)          :\t",sr1.empty,'\t\t',sr2.empty)
      
