Working with mixed datatypes (2)

You have just used np.genfromtxt() to import data containing mixed datatypes. 
There is also another function np.recfromcsv() that behaves similarly to np.genfromtxt(), 
except that its default dtype is None. In this exercise, you'll practice using this to achieve the same result.
Instructions
100xp

    Import titanic.csv using the function np.recfromcsv() and assign it to the variable,
    d. You'll only need to pass file to it because it has the defaults delimiter=',' 
    and names=True in addition to dtype=None!
    Run the remaining code to print the first three entries of the resulting array d.

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d=np.recfromcsv('titanic.csv',delimiter=',',names=True,dtype=None)

# Print out first three entries of d
print(d[:3])

<script.py> output:
    [(1, 0, 3, b'male', 22., 1, 0, b'A/5 21171',  7.25  , b'', b'S')
     (2, 1, 1, b'female', 38., 1, 0, b'PC 17599', 71.2833, b'C85', b'C')
     (3, 1, 3, b'female', 26., 0, 0, b'STON/O2. 3101282',  7.925 , b'', b'S')]
