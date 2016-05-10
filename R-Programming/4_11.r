Wow, that is a lot of cars!

Working with large data sets is not uncommon in data analysis. When you work with 
(extremely) large data sets and data frames, your first task as a data analyst is 
to develop a clear understanding of its structure and main elements. Therefore, 
it is often useful to show only a small part of the entire data set.

So how to do this in R? Well, the function head() enables you to show the first 
observations of a data frame. Similarly, the function tail() prints out the last observations in your data set.

Both head() and tail() print a top line called the 'header', which contains the
names of the different variables in your data set.

Task:

Call head() on the mtcars data set to have a look at the header and the first observations.

Scripts:

# Call head() on mtcars
head(mtcars)

Result:

                   mpg cyl disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
