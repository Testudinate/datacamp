Pandas and The Hello World of SQL Queries!

Here, you'll take advantage of the power of pandas to write the results 
of your SQL query to a DataFrame in one swift line of Python code!

You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. 
Then you'll query the database to select all records from the Album table.

Recall that to select all records from the Orders table in the Northwind
database, Hugo executed the following command:

df = pd.read_sql_query("SELECT * FROM Orders", engine)

Instructions
100xp

    Import the pandas package using the alias pd.
    Using the function create_engine(), create an engine for the SQLite database 
    Chinook.sqlite and assign it to the variable engine.
    Use the pandas function read_sql_query() to assign to the variable df the 
    DataFrame of results from the following query: select all records from the table Album.
    Run the rest of the code to confirm that the DataFrame created by this method 
    is equal to that created by the previous method that you learned.
    
    
    # Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine("sqlite:///Chinook.sqlite")

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("select * from Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?
print(df.equals(df1))


 AlbumId                                  Title  ArtistId
0        1  For Those About To Rock We Salute You         1
1        2                      Balls to the Wall         2
2        3                      Restless and Wild         2
3        4                      Let There Be Rock         1
4        5                               Big Ones         3
True

<script.py> output:
       AlbumId                                  Title  ArtistId
    0        1  For Those About To Rock We Salute You         1
    1        2                      Balls to the Wall         2
    2        3                      Restless and Wild         2
    3        4                      Let There Be Rock         1
    4        5                               Big Ones         3
    True
