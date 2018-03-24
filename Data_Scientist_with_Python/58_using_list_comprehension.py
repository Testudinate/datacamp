Using a list comprehension

This time, you're going to use the lists2dict() function you defined in 
the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.

The lists2dict() function has already been preloaded, together with a couple of 
lists, feature_names and row_lists. feature_names contains the header names of 
the World Bank dataset and row_lists is a list of lists, where each sublist is a
list of actual values of a row from the dataset.

Your goal is to use a list comprehension to generate a list of dicts, where the 
keys are the header names and the values are the row entries.
Instructions
70xp

    Inspect the contents of row_lists by printing the first two lists in row_lists.
    Create a list comprehension that generates a dictionary using lists2dict() 
    for each sublist in row_lists. The keys are from the feature_names list and 
    the values are the row entries in row_lists. Use sublist as your iterator 
    variable and assign the resulting list of dictionaries to list_of_dicts.
    Look at the first two dictionaries in list_of_dicts by printing them out.

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

<script.py> output:
    ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960',
    '133.56090740552298']
    ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']
    {'Value': '133.56090740552298', 'CountryCode': 'ARB', 'Year': '1960', 'IndicatorName': 'Adolescent fertility rate
    (births per 1,000 women ages 15-19)', 'CountryName': 'Arab World', 'IndicatorCode': 'SP.ADO.TFRT'}
    {'Value': '87.7976011532547', 'CountryCode': 'ARB', 'Year': '1960', 'IndicatorName': 'Age dependency ratio 
    (% of working-age population)', 'CountryName': 'Arab World', 'IndicatorCode': 'SP.POP.DPND'}
