To create factors in R, you make use of the function factor(). First thing that you have to do is create a vector that contains all the observations that belong to a limited number of categories. For example, gender_vector contains the sex of 5 different individuals:

gender_vector <- c("Male","Female","Female","Male","Male")
It is clear that there are two categories, or in R-terms 'factor levels', at work here: "Male" and "Female".

The function factor() will encode the vector as a factor:

factor_gender_vector <- factor(gender_vector)

Task:

Convert the character vector gender_vector to a factor with factor() and assign the result to factor_gender_vector
Print out factor_gender_vector and assert that R prints out the factor levels below the actual values.

# Gender vector
gender_vector <- c("Male", "Female", "Female", "Male", "Male")

# Convert gender_vector to a factor
factor_gender_vector <- factor(gender_vector)

# Print out factor_gender_vector
factor_gender_vector

Result:

> # Gender vector
> gender_vector <- c("Male", "Female", "Female", "Male", "Male")
> 
> # Convert gender_vector to a factor
> factor_gender_vector <- factor(gender_vector)
>   
> # Print out factor_gender_vector
> factor_gender_vector
[1] Male   Female Female Male   Male  
Levels: Female Male
