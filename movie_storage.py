API_address = "http://www.omdbapi.com/?apikey=3ea2912d&"


def parses_rating(movie_info):
    """Takes rating as input, this function converts the rating data, and parses
    it into the 'float' type to be useful in functions."""
    rating = movie_info["Ratings"][0]["Value"]
    rating_numerator = rating.split("/")
    float_rating = float(rating_numerator[0])
    return float_rating
