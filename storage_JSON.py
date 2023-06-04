import json
import requests
from istorage import IStorage
from movie_utilities import parses_rating, API_address


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
            Returns a dictionary of dictionaries that
            contains the movies information in the database.

            The function loads the information from the JSON
            file and returns the data.

            For example, the function may return:
            {
              "Titanic": {
                "rating": 9,
                "year": 1999
              },
              "..." {
                ...
              },
            }
            """
        with open(self.file_path, 'r') as file:
            movies = json.loads(file.read())

        return movies

    def add_movie(self, title, year, rating, poster):
        """
            Adds a movie to the movies database.
            Loads the information from the JSON file, add the movie,
            and saves it. The function doesn't need to validate the input.
            """
        movies = self.list_movies()
        movies[title] = {"Year": year, "Rating": rating, "Poster": poster}
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)

    def delete_movie(self, title):
        """
            Deletes a movie from the movies database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
            """
        movies = self.list_movies()
        if title in movies.keys():
            del movies[title]
            with open(self.file_path, 'w') as file:
                json.dump(movies, file)
        else:
            print(f" The film '{title}' doesn't exist")

    def update_movie(self, title, notes):
        """
            Updates a movie from the movies database.
            Loads the information from the JSON file, updates the movie,
            and saves it. The function doesn't need to validate the input.
            """
        movies = self.list_movies()
        # TODO: Address change in param notes/rating
        movies[title]["Rating"] = None  # rating
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)
