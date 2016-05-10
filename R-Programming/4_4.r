When you first get a data set, you will often notice that it contains factors with specific factor levels. 
However, sometimes you will want to change the names of these levels for clarity or other reasons. 
R allows you to do this with the function levels():

levels(factor_vector) <- c("name1", "name2",...)
A good illustration is the raw data that is provided to you by a survey. A standard question for every
questionnaire is the gender of the respondent. You remember from the previous question that this is a 
factor and when performing the questionnaire on the streets its levels are often coded as "M" and "F".

survey_vector <- c("M", "F", "F", "M", "M")
Next, when you want to start your data analysis, your main concern is to keep a nice overview of all
the variables and what they mean. At that point, you will often want to change the factor levels to 
"Male" and "Female" instead of "M" and "F" to make your life easier.

Watch out: the order with which you assign the levels is important. If you type levels(factor_survey_vector), 
you'll see that it outputs [1] "F" "M". If you don't specify the levels of the factor when creating the vector, 
R will automatically assign them alphabetically. To correctly map "F" to "Female" and "M" to "Male", the levels
should be set to c("Female", "Male"), in this order order.

Task:

Check out the code that builds a factor vector from survey_vector. You should use factor_survey_vector in the next instruction.
Change the factor levels of factor_survey_vector to c("Female", "Male"). Mind the order of the vector elements here.

Scripts:

# Code to build factor_survey_vector
survey_vector <- c("M", "F", "F", "M", "M")
factor_survey_vector <- factor(survey_vector)

# Specify the levels of factor_survey_vector
levels(factor_survey_vector) <- c("Female", "Male")

factor_survey_vector

Result:

> # Code to build factor_survey_vector
> survey_vector <- c("M", "F", "F", "M", "M")
> factor_survey_vector <- factor(survey_vector)
> 
> # Specify the levels of factor_survey_vector
> levels(factor_survey_vector) <- 

factor_survey_vector
> # Code to build factor_survey_vector
> survey_vector <- c("M", "F", "F", "M", "M")
> factor_survey_vector <- factor(survey_vector)
> 
> # Specify the levels of factor_survey_vector
> levels(factor_survey_vector) <- c("Female", "Male")
> 
> factor_survey_vector
[1] Male   Female Female Male   Male  
Levels: Female Male
