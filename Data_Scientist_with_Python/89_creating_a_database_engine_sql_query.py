The Hello World of SQL Queries!

Now, it's time for liftoff! In this exercise, you'll perform the Hello
World of SQL queries, SELECT, in order to retrieve all columns of the table Album in 
the Chinook database. Recall that the query SELECT * selects all columns.
Instructions
100xp

    Open the engine connection as con using the method connect() on the engine.
    Execute the query that selects ALL columns from the Album table. Store the results in rs.
    Store all of your query results in the DataFrame df by applying the fetchall() method to the results rs.
    Close the connection!
    
    
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("select * from Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())

<script.py> output:
       0                                      1  2
    0  1  For Those About To Rock We Salute You  1
    1  2                      Balls to the Wall  2
    2  3                      Restless and Wild  2
    3  4                      Let There Be Rock  1
    4  5                               Big Ones  3

