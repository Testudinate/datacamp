Load and explore your Twitter data

Now that you've got your Twitter data sitting locally in a text file, 
it's time to explore it! This is what you'll do in the next few interactive 
exercises. In this exercise, you'll read the Twitter data into a list: tweets_data.
Instructions
100xp

    Assign the filename 'tweets.txt' to the variable tweets_data_path.
    Initialize tweets_data as an empty list to store the tweets in.
    Within the for loop initiated by for line in tweets_file:, load each 
    tweet into a variable, tweet, using json.loads(), then append tweet to 
    tweets_data using the append() method.
    Hit submit and check out the keys of the first tweet dictionary printed to the shell.

# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data=[]

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

<script.py> output:
    dict_keys(['favorite_count', 'lang', 'retweeted_status', 'is_quote_status', 
    'possibly_sensitive', 'geo', 'retweeted', 'timestamp_ms', 'id', 'user', 'extended_entities',
    'retweet_count', 'text', 'contributors', 'id_str', 'created_at', 'in_reply_to_status_id_str', 
    'in_reply_to_user_id', 'entities', 'in_reply_to_screen_name', 'filter_level', 'in_reply_to_status_id', 
    'source', 'favorited', 'in_reply_to_user_id_str', 'truncated', 'coordinates', 'place'])
