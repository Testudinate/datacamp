Ordering your SQL records with ORDER BY

You can also order your SQL query results. For example, if you wanted to get 
all records from the Customer table of the Chinook database and order them in
increasing order by the column SupportRepId, you could do so with the following query:

"SELECT * FROM Customer ORDER BY SupportRepId"

In fact, you can order any SELECT statement by any column.

In this interactive exercise, you'll select all records of the Employee table 
and order them in increasing order by the column BirthDate.

Packages are already imported as follows:

import pandas as pd
from sqlalchemy import create_engine

Get querying!
Instructions
100xp

    Using the function create_engine(), create an engine for the SQLite database 
    Chinook.sqlite and assign it to the variable engine.
    In the context manager, execute the query that selects all records from the 
    Employee table and orders them in increasing order by the column BirthDate. 
    Assign the result to rs.
    In a call to pd.DataFrame(), apply the method fetchall() to rs in order to 
    fetch all records in rs. Store them in the DataFrame df.
    Set the DataFrame's column names to the corresponding names of the table columns.

# Create engine: engine
engine =create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("select * from Employee order by BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())

<script.py> output:
       EmployeeId  LastName FirstName                Title  ReportsTo  \
    0           4      Park  Margaret  Sales Support Agent        2.0   
    1           2   Edwards     Nancy        Sales Manager        1.0   
    2           1     Adams    Andrew      General Manager        NaN   
    3           5   Johnson     Steve  Sales Support Agent        2.0   
    4           8  Callahan     Laura             IT Staff        6.0   
    
                 BirthDate             HireDate              Address        City  \
    0  1947-09-19 00:00:00  2003-05-03 00:00:00     683 10 Street SW     Calgary   
    1  1958-12-08 00:00:00  2002-05-01 00:00:00         825 8 Ave SW     Calgary   
    2  1962-02-18 00:00:00  2002-08-14 00:00:00  11120 Jasper Ave NW    Edmonton   
    3  1965-03-03 00:00:00  2003-10-17 00:00:00         7727B 41 Ave     Calgary   
    4  1968-01-09 00:00:00  2004-03-04 00:00:00          923 7 ST NW  Lethbridge   
    
      State Country PostalCode              Phone                Fax  \
    0    AB  Canada    T2P 5G3  +1 (403) 263-4423  +1 (403) 263-4289   
    1    AB  Canada    T2P 2T3  +1 (403) 262-3443  +1 (403) 262-3322   
    2    AB  Canada    T5K 2N1  +1 (780) 428-9482  +1 (780) 428-3457   
    3    AB  Canada    T3B 1Y7   1 (780) 836-9987   1 (780) 836-9543   
    4    AB  Canada    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772   
    
                          Email  
    0  margaret@chinookcorp.com  
    1     nancy@chinookcorp.com  
    2    andrew@chinookcorp.com  
    3     steve@chinookcorp.com  
    4     laura@chinookcorp.com
