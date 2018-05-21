import webbrowser
import os
import re
# Styles and scripting for the page
main_page_head = '''
<html>
<head>
   <title>Movie Trailers</title>
<meta name = "viewport" content = "width=device-width, initial-scale = 1.0">
<script src = "https://code.jquery.com/jquery-1.12.3.min.js" integrity = "sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
    crossorigin = "anonymous"></script>
    <link href = "https://fonts.googleapis.com/css?family = Courgette" rel = "stylesheet">
    <link rel = "stylesheet" href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel = "stylesheet" type = "text/css" />
<script src = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })
        function changeVideo(id) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + id;
            $("#myVideo").modal("show");
         $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        }
    </script>
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 10%;
            justify-content: center;
        }
        body {
            margin: 0;
            background-color:#eee;
        }
        h1 {
            color: lightseagreen;
            background-color: olivedrab;
            height: 1.5cm;
            text-align: center;
            font-size: 40px;
            font-family: 'cursive', cursive;
        }
        img {
            height: 400px;
            width: 250px;
        }
        .t1:hover,
        .t2:hover,
        .t3:hover,
        .t4:hover,
        .t5:hover,
        .t6:hover
         {
            background-color: lightseagreen;
            cursor: pointer;
        }
        .t1 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eee;
        }
        .t2 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eee;
        }
        .t3 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eee;
        }
        .t4 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eeeeee;
        }
        .t5 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eee;
        }
        .t6 {
            padding-top: 30px;
            padding-left: 50px;
            padding-bottom: 30px;
            padding-right: 50px;
            background-color: #eee;
        }
        </style>
</head>
    '''
main_page_content = '''
 <body>
    <h1> Movie Trailers</h1>
    <main>
        <div class = "container">
            <div class = "t1" onclick = "changeVideo('ZisWjdjs-gM')">
                <img  src = "https://bit.ly/2kf4PpP" alt="Wall-e">
                <figcaption style = "text-align: center; color: white;">
                    <b>Wall-e</b>
                </figcaption>
            </div>
            <div class = "t2" onclick = "changeVideo('Jt1Nv-8_-cg')">
                <img src = "https://bit.ly/2IDio0E" alt="Haripoter">
                <figcaption style = "text-align: center; color: white;">
                    <b>Haripoter</b>
                </figcaption>
            </div>
            <div class = "t3" onclick = "changeVideo('Aahj3atxdS4')">
                <img src = "https://bit.ly/2IYoV5F" alt="Bagamathi">
                <figcaption style = "text-align: center; color: white;">
                    <b>Bagamathi</b>
                </figcaption>
            </div>
            <div class="t4" onclick="changeVideo('d3A3-zSOBT4')">
                <img src="https://bit.ly/2LjqGJ5" alt="Inception">
                <figcaption style="text-align: center; color: white;">
                    <b>Inception</b>
                </figcaption>
            </div>
        <div class="t5" onclick="changeVideo('-kFvrsAgp3M')">
        <img src="https://bit.ly/2s1ikNk" alt="Toliprema">
                <figcaption style="text-align: center; color: white;">
                    <b>ToliPrema</b>
                </figcaption>
            </div>
            <div class="t6" onclick="changeVideo('G62HrubdD6o')">
                <img src="https://bit.ly/2IWZFg8" alt="Bahubali2">
                <figcaption style="text-align: center; color: white;">
                    <b>Bahubali2</b>
                </figcaption>
            </div>
        </div>
        <div class="modal fade" id="myVideo" tabindex="1" role="dialog" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-footer">
                        <button type="button" class="fa fa-close" data-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <iframe id="myframeY" width="100%" height="350px" src="" frameborder="0" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
'''
# A single movie entry html template
movie_title_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-youtube-
id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
   <img src="{poster_image_url}" width="220" height="342">
   <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_titles_content(movies):
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_yout_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_yout_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Append the tile for the movie with its content filled in
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
            )
        return content


def open_movies_page(movies):
    # Append the tile for the movie with its content filled in
    output_file = open('fresh_tomatoes.html', 'w')
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_titles=create_movie_titles_content(movies))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
