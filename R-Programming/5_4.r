Since using built-in data sets is not even half the fun of creating your own data sets, 
the rest of this chapter is based on your personally developed data set. Put your jet
pack on because it is time for some space exploration!

As a first goal, you want to construct a data frame that describes the main characteristics 
of eight planets in our solar system. According to your good friend Buzz, the main features of a planet are:

The type of planet (Terrestrial or Gas Giant).
The planet's diameter relative to the diameter of the Earth.
The planet's rotation across the sun relative to that of the Earth.
If the planet has rings or not (TRUE or FALSE).
After doing some high-quality research on Wikipedia, you feel confident enough to 
create the necessary vectors: name, type, diameter, rotation and rings; these vectors 
have already been coded up on the right. The first element in each of these vectors correspond to the first observation.

You construct a data frame with the data.frame() function. As arguments, you pass 
the vectors from before: they will become the different columns of your data frame.
Because every column has the same length, the vectors you pass should also have 
the same length. But don't forget that it is possible (and likely) that they contain different types of data.

Task:

Use the function data.frame() to construct a data frame. Pass the vectors name, type, 
diameter, rotation and rings as arguments to data.frame(), in this order. Call the resulting data frame planets_df.

Scripts:

# Definition of vectors
name <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", 
          "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)

# Create a data frame from the vectors
planets_df <-data.frame(name,type,diameter,rotation,rings)

REsult:

# Definition of vectors
> name <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
> type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", 
          "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
> diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
> rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
> rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
> 
> # Create a data frame from the vectors
> planets_df <-data.frame(name,type,diameter,rotation,rings)
> planets_df
     name               type diameter rotation rings
1 Mercury Terrestrial planet    0.382    58.64 FALSE
2   Venus Terrestrial planet    0.949  -243.02 FALSE
3   Earth Terrestrial planet    1.000     1.00 FALSE
4    Mars Terrestrial planet    0.532     1.03 FALSE
5 Jupiter          Gas giant   11.209     0.41  TRUE
6  Saturn          Gas giant    9.449     0.43  TRUE
7  Uranus          Gas giant    4.007    -0.72  TRUE
8 Neptune          Gas giant    3.883     0.67  TRUE
