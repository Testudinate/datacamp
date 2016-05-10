Similar to vectors, you can use the square brackets [ ] to select one or multiple elements 
from a matrix. Whereas vectors have one dimension, matrices have two dimensions. You should 
therefore use a comma to separate that what to select from the rows from that what you want 
to select from the columns. For example:

    my_matrix[1,2] selects the element at the first row and second column.
    my_matrix[1:3,2:4] results in a matrix with the data on the rows 1, 2, 3 and columns 2, 3, 4.

If you want to select all elements of a row or a column, no number is needed before or after 
the comma, respectively:

    my_matrix[,1] selects all elements of the first column.
    my_matrix[1,] selects all elements of the first row.

Back to Star Wars with this newly acquired knowledge! As in the previous exercise, 
all_wars_matrix is already available in your workspace.

# all_wars_matrix is available in your workspace
all_wars_matrix

# Select the non-US revenue for all movies
non_us_all <- all_wars_matrix[,2]
  
# Average non-US revenue
mean(non_us_all)
  
# Select the non-US revenue for first two movies
non_us_some <- all_wars_matrix[1:2,2]
  
# Average non-US revenue for first two movies
mean(non_us_some)

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
> # Select the non-US revenue for all movies
> non_us_all <- all_wars_matrix[,2]
>   
> # Average non-US revenue
> mean(non_us_all)
[1] 347.9667
>   
> # Select the non-US revenue for first two movies
> non_us_some <- all_wars_matrix[1:2,2]
>   
> # Average non-US revenue for first two movies
> mean(non_us_some)
[1] 281.15
