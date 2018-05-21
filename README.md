PROJECT1:Movie-trailer
     This project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube.
   If we click on poster we get an youtube trailer of that movie. The project also includes some CSS and jQuery involved in the display of the webpage.
 First we create a html fileand apply some styles using CSS. Put that HTML file inside freshtomatoes.py file.
 FOR SERVER SIDE RUNNING 
Here we are using three python files for running the program in serverside.
They are
 i)media.py 
ii)center.py
iii)freshtomatoes.py
 MEDIA.PY 
   The movie class in the movie.py creates a data structure to store your favorite movies, including movie title,image url and youtube link to the movie trailer.
 CENTER.PY
   This is the main file which creates multiple instances of that movie class to represent my favorite movies.
 FRESHTOMATOES.PY 
   This file has a function called open_movies_Page that takes one argument, which is a list movie trailers and after running this file in server side an html file is created in the same location where
  media.py and center.py file present.
