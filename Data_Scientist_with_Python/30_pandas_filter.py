Driving right (2)

The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.
Instructions
Convert the code on the right to a one-liner that calculates the variable sel as before.


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[cars['drives_right']]
#Nice one! cars contains 7 rows or observations, sel contains 4; so in the majority of the countries in your dataset, 
#people drive on the right side of the road.

# Print sel
print(sel)
