You probably remember from high school that some planets in our solar system have rings
and others do not. But due to other priorities at that time (read: puberty) you can not
recall their names, let alone their rotation speed, etc.

Could R help you out?

If you type rings_vector in the console, you get:

[1] FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE
This means that the first four observations (or planets) do not have a ring (FALSE), 
but the other four do (TRUE). However, you do not get a nice overview of the names
of these planets, their diameter, etc. Let's try to use rings_vector to select the 
data for the four planets with rings.

Task:

The code on the right selects the name column of all planets that have rings.
Adapt the code so that instead of only the name column, all columns for planets that have rings are selected.

Scripts:
# planets_df and rings_vector are pre-loaded in your workspace
# Adapt the code to select all columns for planets with rings
planets_df[rings_vector, ]

Result:

> # planets_df and rings_vector are pre-loaded in your workspace
> 
> # Adapt the code to select all columns for planets with rings
> planets_df[rings_vector, "name"]
[1] Jupiter Saturn  Uranus  Neptune
Levels: Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus
> # planets_df and rings_vector are pre-loaded in your workspace
> 
> # Adapt the code to select all columns for planets with rings
> planets_df[rings_vector, ]
     name      type diameter rotation rings
5 Jupiter Gas giant   11.209     0.41  TRUE
6  Saturn Gas giant    9.449     0.43  TRUE
7  Uranus Gas giant    4.007    -0.72  TRUE
8 Neptune Gas giant    3.883     0.67  TRUE
