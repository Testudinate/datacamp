Checking out the Wikipedia API

You're doing so well and having so much fun that we're going to
throw one more API at you: the Wikipedia API (documented here). You'll 
figure out how to find and extract information from the Wikipedia page for Pizza. What gets a
bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python 
can handle that because it will translate them into dictionaries within dictionaries.

The URL that requests the relevant query from the Wikipedia API is

https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza

Instructions
100xp

    Assign the relevant URL to the variable url.
    Apply the json() method to the response object r and store the resulting
    dictionary in the variable json_data.
    The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; 
    use the function print() to print this string to the shell.

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

<p><b>Pizza</b> is a traditional Italian dish consisting of a yeasted flatbread typically topped with tomato sauce and cheese and baked in an oven. It can also be topped with additional vegetables, meats, and condiments, and can be made without cheese.</p>
<p>The term <i>pizza</i> was first recorded in the 10th century, in a Latin manuscript from the Southern Italian town of Gaeta in Lazio, on the border with Campania. Modern pizza was invented in Naples, and the dish and its variants have since become popular and common in many areas of the world. In 2009, upon Italy's request, Neapolitan pizza was registered with the European Union as a Traditional Speciality Guaranteed dish. The <i>Associazione Verace Pizza Napoletana</i> (True Neapolitan Pizza Association), a non-profit organization founded in 1984 with headquarters in Naples, aims to "promote and protect... the true Neapolitan pizza".</p>
<p>Pizza is one of the most popular foods in the world and a common fast food item in Europe and North America. Many independent or chain restaurants, cafes, and fast food outlets offer pizza. Restaurants or chains specializing in pizza are pizzerias. Pizza delivery is common in some parts of the world.</p>
<p>Pizza is sold fresh or frozen, either whole or in portions. Various types of ovens are used to cook them and many varieties exist. Several similar dishes are prepared from ingredients commonly used in pizza preparation, such as calzone and stromboli. In the United States, pizza is usually eaten out of hand after dividing into slices from a large pizza or small pizzetta as a whole. In Italy, pizza is eaten with a fork and knife in restaurants, but is also sold to take away and eaten out of hand. Frozen pizza became popular in the late 20th century.</p>
<p></p>

<script.py> output:
    <p><b>Pizza</b> is a traditional Italian dish consisting of a yeasted flatbread typically topped with tomato sauce and cheese and baked in an oven. It can also be topped with additional vegetables, meats, and condiments, and can be made without cheese.</p>
    <p>The term <i>pizza</i> was first recorded in the 10th century, in a Latin manuscript from the Southern Italian town of Gaeta in Lazio, on the border with Campania. Modern pizza was invented in Naples, and the dish and its variants have since become popular and common in many areas of the world. In 2009, upon Italy's request, Neapolitan pizza was registered with the European Union as a Traditional Speciality Guaranteed dish. The <i>Associazione Verace Pizza Napoletana</i> (True Neapolitan Pizza Association), a non-profit organization founded in 1984 with headquarters in Naples, aims to "promote and protect... the true Neapolitan pizza".</p>
    <p>Pizza is one of the most popular foods in the world and a common fast food item in Europe and North America. Many independent or chain restaurants, cafes, and fast food outlets offer pizza. Restaurants or chains specializing in pizza are pizzerias. Pizza delivery is common in some parts of the world.</p>
    <p>Pizza is sold fresh or frozen, either whole or in portions. Various types of ovens are used to cook them and many varieties exist. Several similar dishes are prepared from ingredients commonly used in pizza preparation, such as calzone and stromboli. In the United States, pizza is usually eaten out of hand after dividing into slices from a large pizza or small pizzetta as a whole. In Italy, pizza is eaten with a fork and knife in restaurants, but is also sold to take away and eaten out of hand. Frozen pizza became popular in the late 20th century.</p>
    <p></p>
