import movie_storage
import json


def loads_html_file():
    """The function loads and returns the code from the html template file ready for easy access
    in the other functions"""
    with open("index_template.html", "r") as file_obj:
        template_html = file_obj.read()
    return template_html


def replace_html_template_title():
    """to access html file and replace the placeholder text of the title on the page, and
    returns the updated file object"""
    template_html = loads_html_file()
    updated_title_html = template_html.replace("__TEMPLATE_TITLE__", "My Movie Database")
    with open("movies.html", "w") as updated_html_file:
        updated_html_file.write(updated_title_html)
    with open("movies.html", "r") as fileobj:
        updated_title = fileobj.read()
    return updated_title


def serialize_movie_data(movie, info):
    """to serialize one dictionary item (key/value) to the correct string format for website generation. This accesses the title,
    the year, and poster url and formats them into appropriate html and accessing the CSS classes
    so that they appear correctly on the webpage, and then returns that string"""
    movie_data_str = ""
    movie_title = movie
    movie_year = info["Year"]
    if "Poster" in info:
        movie_poster = info["Poster"]
    else:
        movie_poster = "data:image/png;base64,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"

    movie_data_str += '<li><div class="movie">'
    movie_data_str += f'<img class="movie-poster" src="{movie_poster}">'

    if movie_title:
        movie_data_str += '<div class="movie-title">'
        movie_data_str += f'{movie_title}</div>'

    if movie_year:
        movie_data_str += '<div class = "movie-year">'
        movie_data_str += f'{movie_year}</div>'

    movie_data_str += '</div></li>'
    return movie_data_str


def parses_movie_data():
    """Loops through the whole dictionary applying the serializing function to each dictionary item, creating
    one long string and then returns that string to be used in html generation"""
    movie_data = movie_storage.list_movies()
    movie_data_str = ""
    for movie, info in movie_data.items():
        movie_data_str += serialize_movie_data(movie, info)
    return movie_data_str


def create_website():
    """This function generates the website - it parses the movie data using the previous functions and saves as
    a variable, then updates the title placeholder in the template html file, whilst creating a new file. This is then
    updated again via replacing the template movie grid text with the movie data that has been parsed, and re-writes
    the file"""
    movie_data = parses_movie_data()
    updated_title_html = replace_html_template_title()
    updated_html_movie_data = updated_title_html.replace("__TEMPLATE_MOVIE_GRID__", movie_data)
    with open("movies.html", "w") as updated_movie_html_file:
        updated_movie_html_file.write(updated_html_movie_data)

