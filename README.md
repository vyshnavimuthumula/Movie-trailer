## PROJECT1: Movie-trailer
   This project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a      
listing  of favorite movies and links each movie to its trailers video on YouTube.If we click on poster we get an youtube      trailer of that movie. The project also includes some CSS and jQuery involved in the display of the webpage.
### STEPS:   
 First we create a html file and apply some styles using CSS. Put that HTML file inside freshtomatoes.py file.
### FOR SERVER SIDE RUNNING:  
Here we are using three python files for running the program in serverside.  
They are  
i)media.py  
ii)center.py  
iii)freshtomatoes.py

### MEDIA.PY
   The movie class in the movie.py creates a data structure to store your favorite movies, including movie title,image url and youtube link to the movie trailer.

### CENTER.PY
   This is the main file which creates multiple instances of that movie class to represent my favorite movies.
   
### FRESHTOMATOES.PY 
   This file has a function called open_movies_Page that takes one argument, which is a list movie trailers and data about movie.
  These three files are kept inside cgi-bin folder. (Because all python files are kept inside the python file)
   1)If we run center.py file in shell automatically a webpage will open and html file was created inside the bin.
  ### Process For server side running 
  i)In windows
     Go to the cgi-bin where our project is present and open terminal then type
       #### python -m http.server --cgi 8888
     8888 is a port numberand we can write any port number.
   ii)In Linux
      Go to outside of cgi-bin and open terminal then type
       #### python -m CGIHTTPServer 8888
  after running this file in server side an html file is created outside the bin.
  After running server go to the webbrowser and type localhost:8888.
  Then it displays cgi-bin click on it and open center.py finally our project will display on the browser.
  
