import csv
from istorage import IStorage


class StorageCSV(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the CSV
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
        movies = {}
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies[row['Title']] = {
                    'Rating': float(row['Rating']),
                    'Year': int(row['Year']),
                    'Poster': row['Poster']
                }
        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies database.
        Loads the information from the CSV file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.list_movies()
        movies[title] = {"Rating": rating, "Year": year, "Poster": poster}
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Rating', 'Year', 'Poster'])
            writer.writeheader()
            for movie_title, movie_data in movies.items():
                writer.writerow({
                    'Title': movie_title,
                    'Rating': movie_data['Rating'],
                    'Year': movie_data['Year'],
                    'Poster': movie_data['Poster']
                })

    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the CSV file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.list_movies()
        if title in movies.keys():
            del movies[title]
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Title', 'Rating', 'Year', 'Poster'])
                writer.writeheader()
                for movie_title, movie_data in movies.items():
                    writer.writerow({
                        'Title': movie_title,
                        'Rating': movie_data['Rating'],
                        'Year': movie_data['Year'],
                        'Poster': movie_data['Poster']
                    })
        else:
            print(f" The film '{title}' doesn't exist")

    def update_movie(self, title, notes):
        """
        Updates a movie from the movies database.
        Loads the information from the CSV file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.list_movies()
        # TODO: Address change in param notes/rating
        movies[title]["Rating"] = None  # rating
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Rating', 'Year', 'Poster'])
            writer.writeheader()
            for movie_title, movie_data in movies.items():
                writer.writerow({
                    'Title': movie_title,
                    'Rating': movie_data['Rating'],
                    'Year': movie_data['Year'],
                    'Poster': movie_data['Poster']
                })

