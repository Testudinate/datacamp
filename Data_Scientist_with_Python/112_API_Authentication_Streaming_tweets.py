Streaming tweets

Now that you have set up your authentication credentials, it is time to stream some tweets! 
We have already defined the tweet stream listener class, MyStreamListener, just as Hugo did 
in the introductory video. You can find the code for the tweet stream listener class here.

Your task is to create the Streamobject and to filter tweets according to particular keywords.
Instructions
100xp

    Create your Stream object with authentication by passing tweepy.Stream() the authentication 
    handler auth and the Stream listener l;
    To filter Twitter streams, pass to the track argument in stream.filter() a list containing
    the desired keywords 'clinton', 'trump', 'sanders', and 'cruz'.


# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
