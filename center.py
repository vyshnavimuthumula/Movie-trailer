#!/usr/bin/env python
print("Content-type:text/html \n")
import media
import fresh_tomatoes

a = media.Movie("Wall-e","Robot left on earth","https://images-na.ssl-images-amazon.com/images/I/51RoZRgIHtL.jpg"
                    ,"https://www.youtube.com/embed/ZisWjdjs-gM")
b=media.Movie("Harrypoter","dadlove"
              ,"https://vignette.wikia.nocookie.net/harrypotter/images/6/65/Harry-Potter-and-the-Deathly-Hallows-Part-1-poster.jpg/revision/latest?cb=20101001182826"
              ,"https://www.youtube.com/embed/Jt1Nv-8_-cg")
c=media.Movie("Bagamathi"," story of Queen Bhaagamathie","https://bestoftheyear.in/wp-content/uploads/2018/02/Bhaagamathie-1-400x567.jpg"
              ,"https://www.youtube.com/embed/Aahj3atxdS4")
d=media.Movie("Inception","In dream story","https://images-na.ssl-images-amazon.com/images/I/61Ug%2BK8o5FL.jpg"
              ,"https://www.youtube.com/embed/d3A3-zSOBT4")
e=media.Movie("Toliprema","firstlove","https://www.comingtrailer.com/images/poster/Tholi-Prema7.jpg"
                    ,"https://www.youtube.com/embed/-kFvrsAgp3M")
f=media.Movie("Bahubali2","old","https://images-na.ssl-images-amazon.com/images/I/61fhQI78YpL._SY550_.jpg","http://www.youtube.com/embedded/G62HrubdD6o")

movies = [a,b,c,d,e,f]
fresh_tomatoes.open_movies_page(movies)
