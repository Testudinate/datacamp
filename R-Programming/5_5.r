The planets_df data frame should have 8 observations and 5 variables.
It has been made available in the workspace, so you can directly use it.

Use str() to investigate the structure of the new planets_df variable.

Scripts:

# Check the structure of planets_df
str(planets_df)

Result:

> # Check the structure of planets_df
> str(planets_df)
'data.frame':	8 obs. of  5 variables:
 $ name    : Factor w/ 8 levels "Earth","Jupiter",..: 4 8 1 3 2 6 7 5
 $ type    : Factor w/ 2 levels "Gas giant","Terrestrial planet": 2 2 2 2 1 1 1 1
 $ diameter: num  0.382 0.949 1 0.532 11.209 ...
 $ rotation: num  58.64 -243.02 1 1.03 0.41 ...
 $ rings   : logi  FALSE FALSE FALSE FALSE TRUE TRUE ...
