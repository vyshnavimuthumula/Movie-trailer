import webbrowser


class Movie():
    """ Class for representing a movie """

    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

    def __init__(self,
                 movie_title, m_storyline, poster_image, trailer_youtube):
        """ Inits a Movie object
        Arguments:
        movie_title = a string of the movie's title
        m_storyline = summery of the movie
        poster_image = a string containing a URL to a poster image
        trailer_yout = a string containing a youtube URL of the movie's trailer
        """
        self.title = movie_title
        self.storyline = m_storyline
        self.poster_image_url = poster_image
        self.trailer_yout_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
