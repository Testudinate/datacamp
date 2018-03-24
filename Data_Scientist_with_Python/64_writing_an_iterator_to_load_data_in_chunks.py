Writing an iterator to load data in chunks (1)

Another way to read data too large to store in memory in chunks is to 
read the file in as DataFrames of a certain length, say, 100. For example, 
with the pandas package (imported as pd), you can do pd.read_csv(filename, chunksize=100). 
This creates an iterable reader object, which means that you can use next() on it.

In this exercise, you will read a file in small DataFrame chunks with read_csv(). 
You're going to use the World Bank Indicators data 'ind_pop.csv', available 
in your current directory, to look at the urban population indicator for numerous countries and years.
Instructions
100xp

    Use pd.read_csv() to read in 'ind_pop.csv' in chunks 
    of size 10. Assign the result to df_reader.
    Print the first two chunks from df_reader.
    
    
 # Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))

IndicatorName      IndicatorCode  Year      Value  
10  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  12.236046  
11  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.680332  
12  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  56.107863  
13  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  64.285435  
14  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  49.284688  
15  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.863308  
16  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960   9.616261  
17  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  21.272894  
18  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  11.498396  
19  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  19.810513
