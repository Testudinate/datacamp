Making and creating rankings is one of mankind's favorite affairs.
These rankings can be useful (best universities in the world), 
entertaining (most influential movie stars) or pointless (best 007 look-a-like).

In data analysis you can sort your data according to a certain variable 
in the data set. In R, this is done with the help of the function order().

order() is a function that gives you the ranked position of each element 
when it is applied on a variable, such as a vector for example:

> a <- c(100, 10, 1000)
> order(a)
[1] 2 1 3
10, which is the second element in a, is the smallest elements, so 2 comes
first in the output of order(a). 100, which is the first element in a is 
the second smallest element, so 1 comes second in the output of order(a).

This means we can use the output of order(a) to reshuffle a:

> a[order(a)]
[1]   10  100 1000

Task:

Experiment with the order() function in the console. Click 'Submit Answer' when you are ready to continue.

Scripts:

# Play around with the order function in the console

order()

Result:

> # Play around with the order function in the console
> 
> order()
NULL
> 
