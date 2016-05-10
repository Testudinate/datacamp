Similar to what you have learned with vectors, the standard operators like +, -, /, *, etc. work
in an element-wise way on matrices in R.

For example, 2 * my_matrix multiplies each element of my_matrix by two.

As a newly-hired data analyst for Lucasfilm, it is your job is to find out how many visitors 
went to each movie for each geographical area. You already have the total revenue figures in 
all_wars_matrix. Assume that the price of a ticket was 5 dollars. Simply dividing the box office 
numbers by this ticket price gives you the number of visitors.


    Divide all_wars_matrix by 5, giving you the number of visitors in millions. Assign the resulting matrix to visitors.
    Print out visitors so you can have a look.

# all_wars_matrix is available in your workspace
all_wars_matrix

# Estimate the visitors
visitors <- all_wars_matrix/5
  
# Print the estimate to the console
visitors


Result:

> # all_wars_matrix is available in your workspace
> all_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
> 
> # Estimate the visitors
> visitors <- all_wars_matrix/5
>   
> # Print the estimate to the console
> visitors
                           US non-US
A New Hope              92.20  62.88
The Empire Strikes Back 58.10  49.58
Return of the Jedi      61.86  33.16
The Phantom Menace      94.90 110.50
Attack of the Clones    62.14  67.74
Revenge of the Sith     76.06  93.70
> 
