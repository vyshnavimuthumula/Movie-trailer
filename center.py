import media
import fresh_tomatoes

"""
declare favorite movies, with 4 args each:
title (movie's title)
storyline (summery of the ovie)
poster_image (url to poster image)
trailer_youtube (url to youtube trailer)
"""
walle = media.Movie(
  "Wall-e",
  "Robot left on earth",
  "https://bit.ly/2kf4PpP",
  "https://www.youtube.com/embed/ZisWjdjs-gM")
harrypoter = media.Movie(
  "Harrypoter",
  "story of a boy",
  "https://bit.ly/2IDio0E",
  "https://www.youtube.com/embed/Jt1Nv-8_-cg")
bagamathi = media.Movie(
  "Bagamathi",
  " story of Queen Bhaagamathie",
  "https://bit.ly/2IYoV5F",
  "https://www.youtube.com/embed/Aahj3atxdS4")
inception = media.Movie(
  "Inception",
  "In dream story",
  "https://bit.ly/2LjqGJ5",
  "https://www.youtube.com/embed/d3A3-zSOBT4")
toliprema = media.Movie(
  "Toliprema",
  "firstlove",
  "https://bit.ly/2s1ikNk",
  "https://www.youtube.com/embed/-kFvrsAgp3M")
bahubali2 = media.Movie(
  "Bahubali2",
  "old",
  "https://bit.ly/2IWZFg8",
  "http://www.youtube.com/embedded/G62HrubdD6o")

# assign individual movies to movies list
movies = [walle, harrypoter, bagamathi, inception, toliprema, bahubali2]

# call movie trailer page method and pass movies list and sorting option
fresh_tomatoes.open_movies_page(movies)
