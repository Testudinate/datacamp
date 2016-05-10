Being a huge movie fan (remember your job at LucasFilms), you decide to start storing information 
on good movies with the help of lists.

Start by creating a list for the movie "The Shining". We have already created the variables mov,
act and rev in your R workspace. Feel free to check them out in the console.

Instructions
Complete the code on the right to create shining_list; it contains three elements:

moviename: a character string with the movie title (stored in mov)
actors: a vector with the main actors' names (stored in act)
reviews: a data frame that contains some reviews (stored in rev)
Do not forget to name the list components accordingly (names are moviename, actors and reviews).

Scripts:

# The variables mov, act and rev are available

# Finish the code to build shining_list
shining_list <- list(moviename = mov, actors = act, reviews = rev)

Result:

> # The variables mov, act and rev are available
> 
> # Finish the code to build shining_list
> shining_list <- list(moviename = mov, actors = act, reviews = rev)
> # The variables mov, act and rev are available
> 
> # Finish the code to build shining_list
> shining_list <- list(moviename = mov, actors = act, reviews = rev)
> shining_list
$moviename
[1] "The Shining"

$actors
[1] "Jack Nicholson"   "Shelley Duvall"   "Danny Lloyd"      "Scatman Crothers"
[5] "Barry Nelson"    

$reviews
  scores sources                                              comments
1    4.5   IMDb1                     Best Horror Film I Have Ever Seen
2    4.0   IMDb2 A truly brilliant and scary film from Stanley Kubrick
3    5.0   IMDb3                 A masterpiece of psychological horror

