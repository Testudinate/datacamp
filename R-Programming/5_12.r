Alright, now that you understand the order() function, let us 
do something useful with it. You would like to rearrange your 
data frame such that it starts with the smallest planet and ends 
with the largest one. A sort on the diameter column.

Task:

Call order() on planets_df$diameter (the diameter column of planets_df). Store the result as positions.
Now reshuffle planets_df with the positions vector as row indexes inside square brackets. 
Keep all columns. Simply print out the result.

Scripts:

# planets_df is pre-loaded in your workspace

# Use order() to create positions
positions <-  order(planets_df$diameter)

# Use positions to sort planets_df

planets_df[positions,]

Result:

> planets_df[positions,]
     name               type diameter rotation rings
1 Mercury Terrestrial planet    0.382    58.64 FALSE
4    Mars Terrestrial planet    0.532     1.03 FALSE
2   Venus Terrestrial planet    0.949  -243.02 FALSE
3   Earth Terrestrial planet    1.000     1.00 FALSE
8 Neptune          Gas giant    3.883     0.67  TRUE
7  Uranus          Gas giant    4.007    -0.72  TRUE
6  Saturn          Gas giant    9.449     0.43  TRUE
5 Jupiter          Gas giant   11.209     0.41  TRUE

