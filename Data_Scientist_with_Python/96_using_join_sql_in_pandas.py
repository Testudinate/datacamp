Filtering your INNER JOIN

Congrats on performing your first INNER JOIN! You're now going to finish 
this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.

Recall that to INNER JOIN the Orders and Customers tables from the Northwind 
database, Hugo executed the following SQL query:

"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"

The following code has already been executed to import the neccesary packages 
and to create the engine:

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

Instructions
100xp

    Use the pandas function read_sql_query() to assign to the variable df the
    DataFrame of results from the following query: select all records from 
    PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId 
    that satisfy the condition Milliseconds < 250000.
    
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("select * from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId where Milliseconds < 250000 ", engine)

# Print head of DataFrame
print(df.head())

<script.py> output:
       PlaylistId  TrackId  TrackId              Name  AlbumId  MediaTypeId  \
    0           1     3390     3390  One and the Same      271            2   
    1           1     3392     3392     Until We Fall      271            2   
    2           1     3393     3393     Original Fire      271            2   
    3           1     3394     3394       Broken City      271            2   
    4           1     3395     3395          Somedays      271            2   
    
       GenreId Composer  Milliseconds    Bytes  UnitPrice  
    0       23     None        217732  3559040       0.99  
    1       23     None        230758  3766605       0.99  
    2       23     None        218916  3577821       0.99  
    3       23     None        228366  3728955       0.99  
    4       23     None        213831  3497176       0.99
