Using pandas to import flat files as DataFrames (1)

In the last exercise, you were able to import flat files containing
columns with different datatypes as numpy arrays. However, the DataFrame 
object in pandas is a more appropriate structure in which to store such data and, 
thankfully, we can easily import files of mixed data types as DataFrames using 
the pandas functions read_csv() and read_table().
Instructions
100xp

    Import the pandas package using the alias pd.
    Read titanic.csv into a DataFrame called df. The file name is already stored in the file object.
    In a print() call, view the head of the DataFrame.

# Import pandas as pd
import pandas as pd 

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())


   PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch  \
0            1         0       3    male  22.0      1      0   
1            2         1       1  female  38.0      1      0   
2            3         1       3  female  26.0      0      0   
3            4         1       1  female  35.0      1      0   
4            5         0       3    male  35.0      0      0   

             Ticket     Fare Cabin Embarked  
0         A/5 21171   7.2500   NaN        S  
1          PC 17599  71.2833   C85        C  
2  STON/O2. 3101282   7.9250   NaN        S  
3            113803  53.1000  C123        S  
4            373450   8.0500   NaN        S
