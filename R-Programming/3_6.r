Just like every action has a reaction, every cbind() has an rbind(). (We admit, we are pretty bad with metaphors.)

Your R workspace, where all variables you defined 'live' (check out what a workspace is), 
has already been initialized and contains two matrices:

    star_wars_matrix that we have used all along, with data on the first trilogy,
    star_wars_matrix2, with similar data for the second trilogy.

Type the name of these matrices in the console and hit Enter if you want to have a closer 
look. If you want to check out the contents of the workspace, you can type ls() in the console.

Use rbind() to paste together star_wars_matrix and star_wars_matrix2, in this order.
Assign the resulting matrix to all_wars_matrix.

Scripts:

# star_wars_matrix and star_wars_matrix2 are available in your workspace
star_wars_matrix  
star_wars_matrix2 

# Combine both Star Wars trilogies in one matrix
all_wars_matrix <- rbind(star_wars_matrix,star_wars_matrix2)

Result:
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
> star_wars_matrix2 
                        US non-US
The Phantom Menace   474.5  552.5
Attack of the Clones 310.7  338.7
Revenge of the Sith  380.3  468.5
> 
> # Combine both Star Wars trilogies in one matrix
> all_wars_matrix <- rbind(star_wars_matrix,star_wars_matrix2)
> all_wars_matrix

>>>>>>>>>>>>>>>>Final !!!
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
