Just like every cbind() has a rbind(), every colSums() has a rowSums(). 
Your R workspace already contains the all_wars_matrix that you constructed 
in the previous exercise; type all_wars_matrix to have another look. 
Let's now calculate the total box office revenue for the entire saga.


    Calculate the total revenue for the US and the non-US region and assign total_revenue_vector. 
    You can use the colSums() function.
    Print out total_revenue_vector to have a look at the results.
    
Scripts:

# all_wars_matrix is available in your workspace
all_wars_matrix

# Total revenue for US and non-US
total_revenue_vector <- colSums(all_wars_matrix)
  
# Print out total_revenue_vector
total_revenue_vector
    
Result:
    US non-US 
2226.3 2087.8 

