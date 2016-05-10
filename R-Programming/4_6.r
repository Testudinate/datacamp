In factor_survey_vector we have a factor with two levels: Male and Female. 
But how does R value these relatively to each other? In other words, 
who does R think is better, males or females?

Read the code in the editor and click 'Submit Answer' to see whether males are worth more than females.

Scripts:

# Build factor_survey_vector with clean levels
survey_vector <- c("M", "F", "F", "M", "M")
factor_survey_vector <- factor(survey_vector)
levels(factor_survey_vector) <- c("Female", "Male")

# Male
male <- factor_survey_vector[1] 
male
# Female
female <- factor_survey_vector[2]
female

# Battle of the sexes: Male 'larger' than female?
male > female

Result:
> # Build factor_survey_vector with clean levels
> survey_vector <- c("M", "F", "F", "M", "M")
> factor_survey_vector <- factor(survey_vector)
> levels(factor_survey_vector) <- c("Female", "Male")
> 
> # Male
> male <- factor_survey_vector[1] 
> male
[1] Male
Levels: Female Male
> # Female
> female <- factor_survey_vector[2]
> female
[1] Female
Levels: Female Male
> 
> # Battle of the sexes: Male 'larger' than female?
> male > female
Warning message: '>' not meaningful for factors
[1] NA
