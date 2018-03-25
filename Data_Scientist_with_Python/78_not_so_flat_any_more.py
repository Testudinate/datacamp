Not so flat any more

In Chapter 1, you learned how to use the IPython magic command ! ls to explore your 
current working directory. You can also do this natively in Python using the library os, 
which consists of miscellaneous operating system interfaces.

The first line of the following code imports the library os, the second line stores
the name of the current directory in a string called wd and the third outputs the contents of
the directory in a list to the shell.

import os
wd = os.getcwd()
os.listdir(wd)

Run this code in the IPython shell and answer the following questions. Ignore the files
that begin with ..

Check out the contents of your current directory and answer the following questions: (1)
which file is in your directory and NOT an example of a flat file; (2) why is it not a flat file?
Instructions
50xp
Possible Answers

    database.db is not a flat file because relational databases contain structured relationships and flat files do not.
    press 1
    battledeath.xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table.
    press 2
    titanic.txt is not a flat file because it is a .txt, not a .csv.
    press 3
    
    In [6]: wd
Out[6]: '/tmp/tmpf3p18np3'

In [7]: os.listdir(wd)
Out[7]: ['titanic_corrupt.txt', 'figure.svg', 'titanic.txt', 'battledeath.xlsx']

    
    battledeath.xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table.
