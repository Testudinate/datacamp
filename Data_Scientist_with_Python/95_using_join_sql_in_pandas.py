The power of SQL lies in relationships between tables: INNER JOIN

Here, you'll perform your first INNER JOIN! You'll be working with your

favourite SQLite database, Chinook.sqlite. For each record in the Album table, 
you'll extract the Title along with the Name of the Artist. The latter will come 
from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.

Recall that to INNER JOIN the Orders and Customers tables from the Northwind
database, Hugo executed the following SQL query:

"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.
CustomerID = Customers.CustomerID"

The following code has already been executed to import the necessary packages and to create the engine:

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

Instructions
100xp
Instructions
100xp

    Assign to rs the results from the following query: select all the records, 
    extracting the Title of the record and Name of the artist of each record 
    from the Album table and the Artist table, respectively. To do so, INNER 
    JOIN these two tables on the ArtistID column of both.
    In a call to pd.DataFrame(), apply the method fetchall() to rs in order to
    fetch all records in rs. Store them in the DataFrame df.
    Set the DataFrame's column names to the corresponding names of the table columns.

Hint

    Apply the execute() method on the engine connection and pass to it your SQL query.
    Don't forget to pass to rs.fetchall() as an argument to pd.DataFrame() and assign the result of this to df.
    Recall that you can set the DataFrame's column names by assigning rs.keys() to df.columns.

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("select al.title,ar.name from Album al inner join Artist ar on ar.ArtistId=al.ArtistId")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())

<script.py> output:
                                       Title       Name
    0  For Those About To Rock We Salute You      AC/DC
    1                      Balls to the Wall     Accept
    2                      Restless and Wild     Accept
    3                      Let There Be Rock      AC/DC
    4                               Big Ones  Aerosmith
