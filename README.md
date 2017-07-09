# Movie Trailer Website
Movie Trailer Website server-side code to store a list of your favorite movies, and then generate a static web page allowing visitors to browse their movies and watch the trailers.

### Modules used in the program
_These are the modules that user need to be familiar with_
   - webbrowser
   - os
   - re

### Working
- media.py contains the class that is used to generate objects or instances of your favorite movies, also this class contain the most important functionality of the website that being showing the trailer of your favorite movies.
- tomatoes.py is the static page generator, this contains a function open_movie_page() that takes data structure as an argument and generates a static page.
- entertainment-center.py is the center of the program here all the movie instances or objects are created and list of movies is also created here.
