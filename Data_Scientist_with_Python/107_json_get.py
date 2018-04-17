Loading and exploring a JSON

Now that you know what a JSON is, you'll load one into your Python
environment and explore it yourself. Here, you'll load the JSON 'a_movie.json'
into the variable json_data, which will be a dictionary. You'll then explore the JSON contents
by printing the key-value pairs of json_data to the shell.
Instructions
100xp

    Load the JSON 'a_movie.json' into the variable json_data within the context 
    provided by the with statement. To do so, use the function json.load() within the context manager.
    Use a for loop to print all key-value pairs in the dictionary json_data. Recall that you
    can access a value in a dictionary using the syntax: dictionary[key].

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

<script.py> output:
    Language:  English, French
    Rated:  PG-13
    imdbID:  tt1285016
    Released:  01 Oct 2010
    Runtime:  120 min
    imdbVotes:  537,084
    DVD:  11 Jan 2011
    Director:  David Fincher
    Title:  The Social Network
    Poster:  https://ia.media-imdb.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg
    Metascore:  95
    Production:  Columbia Pictures
    Genre:  Biography, Drama
    Response:  True
    Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)
    Plot:  Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.
    imdbRating:  7.7
    Ratings:  [{'Source': 'Internet Movie Database', 'Value': '7.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '96%'}, {'Source': 'Metacritic', 'Value': '95/100'}]
    Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons
    Year:  2010
    Type:  movie
    Country:  USA
    Awards:  Won 3 Oscars. Another 165 wins & 168 nominations.
    BoxOffice:  $96,400,000
    Website:  http://www.thesocialnetwork-movie.com/
