import requests

API_address = "http://www.omdbapi.com/?apikey=3ea2912d&"


def parses_rating(movie_info):
    """Takes rating as input, this function converts the rating data, and parses
    it into the 'float' type to be useful in functions."""
    rating = movie_info["Ratings"][0]["Value"]
    rating_numerator = rating.split("/")
    float_rating = float(rating_numerator[0])
    return float_rating


def get_movie_details_by_name(movie_name):
    """To receive a user input for a movie name, and contact an API using this input
    to search for the movie, and return the required movie details i.e. title, rating, year
    of release and poster url. Returns dict: {"Year": year, "Rating": rating, "Poster": poster} """
    movie_to_add = requests.get(API_address, params={'t': f'{movie_name}', 'r': 'json'}).json()
    if movie_to_add["Response"] == "False":
        return None
    else:
        year = movie_to_add["Year"]
        rating = parses_rating(movie_to_add)
        poster = movie_to_add["Poster"]
        return {"Year": year, "Rating": rating, "Poster": poster}
