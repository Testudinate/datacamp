Well done, you're on a roll!

Just like on your to-do list, you want to avoid not knowing or remembering what
the components of your list stand for. That is why you should give names to them:

my_list <- list(name1 = your_comp1, 
                name2 = your_comp2)
This creates a list with components that are named name1, name2, and so on. If
you want to name your lists after you've created them, you can use the names()
function as you did with vectors. The following commands are fully equivalent to the assignment above:

my_list <- list(your_comp1, your_comp2)
names(my_list) <- c("name1", "name2")

Task:
Change the code of the previous exercise (see editor) by adding names to the components. 
Use for my_vector the name vec, for my_matrix the name mat and for my_df the name df.
Print out my_list so you can inspect the output.

Scripts:

# Vector with numerics from 1 up to 10
my_vector <- 1:10 

# Matrix with numerics from 1 up to 9
my_matrix <- matrix(1:9, ncol = 3)

# First 10 elements of the built-in data frame mtcars
my_df <- mtcars[1:10,]

# Adapt list() call to give the components names
my_list <- list(vec = my_vector, mat = my_matrix, df = my_df)

# Print out my_list
my_list

Result:

> # Vector with numerics from 1 up to 10
> my_vector <- 1:10 
> 
> # Matrix with numerics from 1 up to 9
> my_matrix <- matrix(1:9, ncol = 3)
> 
> # First 10 elements of the built-in data frame mtcars
> my_df <- mtcars[1:10,]
> 
> # Adapt list() call to give the components names
> my_list <- list(vec = my_vector, mat = my_matrix, df = my_df)
> 
> # Print out my_list
> my_list
$vec
 [1]  1  2  3  4  5  6  7  8  9 10

$mat
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9

$df
                   mpg cyl  disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
Duster 360        14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
Merc 240D         24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
Merc 230          22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
Merc 280          19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
