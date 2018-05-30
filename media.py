import webbrowser		# Imports the module Webbrowser


class Movie():
    """ This class provides movie realted information. 
    Info like movie title, storyline, poster image,
    trailer is displayed of each movie. """

    # List of ratings that can be given to a movie
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # A constructor to initialize instance variables
    def __init__(self, movie_title, movie_storyline, movie_poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer

    def show_trailer(self): 					# A method to open the movie trailer
        webbrowser.open(self.trailer_youtube_url)
