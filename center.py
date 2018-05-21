import media
import fresh_tomatoes

walle = media.Movie(
  "Wall-e",
  "Robot left on earth",
  "https://images-na.ssl-images-amazon.com/images/I/51RoZRgIHtL.jpg",
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
  "https://images-na.ssl-images-amazon.com/images/I/61Ug%2BK8o5FL.jpg",
  "https://www.youtube.com/embed/d3A3-zSOBT4")
toliprema = media.Movie(
  "Toliprema",
  "firstlove",
  "https://www.comingtrailer.com/images/poster/Tholi-Prema7.jpg",
  "https://www.youtube.com/embed/-kFvrsAgp3M")
bahubali2 = media.Movie(
  "Bahubali2",
  "old",
  "https://images-na.ssl-images-amazon.com/images/I/61fhQI78YpL._SY550_.jpg",
  "http://www.youtube.com/embedded/G62HrubdD6o")

movies = [walle, harrypoter, bagamathi, inception, toliprema, bahubali2]
fresh_tomatoes.open_movies_page(movies)
