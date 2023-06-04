import statistics
import requests
import random
import movies_website_creation
from istorage import IStorage
from movie_utilities import get_movie_details_by_name
from storage_JSON import StorageJson


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        """When selected from menu will print the list of all the movies available in the data"""
        movies = self._storage.list_movies()
        movies_in_total = len(movies)
        print(f"{movies_in_total} movies in total")
        for movie_name, info in movies.items():
            print(f"""{movie_name}: Rated {info["Rating"]}\nYear of release {info["Year"]}""")

    def get_list_movie_ratings(self):
        """Creates a list of the ratings of the movies, and is useful to use in other functions"""
        movies = self._storage.list_movies()
        movie_ratings = []
        for rating in movies.values():
            movie_ratings.append(rating["Rating"])
        return movie_ratings

    def _command_movie_stats(self):
        """Produces some statistics for the movies in the database, including the average rating, the median rating,
            the best and worst movies."""
        movies = self._storage.list_movies()
        ratings = self.get_list_movie_ratings()
        average_rating = statistics.mean(ratings)
        median_rating = statistics.median(ratings)

        best_movies = []
        worst_movies = []
        highest_rating = max(ratings)
        lowest_rating = min(ratings)
        for movie, info in movies.items():
            if info["Rating"] == highest_rating:
                best_movies.append(movie)
            if info["Rating"] == lowest_rating:
                worst_movies.append(movie)

        print(f"Average rating: {average_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movie(s): {best_movies}")
        print(f"Worst movie(s): {worst_movies}")

    def add_movie(self):
        """Prompts the user to enter the title, rating and year of release of the movie they would like to add
        to the database, and then adds that movie data to the database"""
        try:
            movies = self._storage.list_movies()
            new_movie_name = input("Please enter the name of the movie you would like to add: ")
            if new_movie_name in movies:
                print(f"Movie {new_movie_name} already exists!")
                return

            movie_details = get_movie_details_by_name(new_movie_name)
            if movie_details is None:
                print(f"I'm sorry, {new_movie_name} doesn't exist in the database.")
            else:
                movies = self._storage.add_movie(new_movie_name, movie_details["Year"], movie_details["Rating"], movie_details["Poster"])
                print(f"Movie {new_movie_name} successfully added")
        except requests.exceptions.RequestException as connection_error:
            print(f"I'm sorry, there has been an error: {connection_error}")

    def exit_application(self):
        """Exits the application"""
        print("Bye!")
        exit()

    def delete_movie(self):
        """Prompts user to enter the name of the movie they want to delete, and then deletes that movies
        entire info from the database"""
        movie_title_to_delete = input("Please enter the name of the movie you would like to delete: ")
        self._storage.delete_movie(movie_title_to_delete)

    def update_movie(self):
        """To update a movies rating, the user is prompted to enter the title, it is searched for and if
        found asks the user for the new rating and then updates the database, otherwise if not found
        tells the user that that movie does not exist in the database."""
        movies = self._storage.list_movies()
        movie_title_to_update = input("Please enter the name of the movie you wish to update: ")
        if movie_title_to_update in movies:
            new_movie_rating = input("Please enter the new movie rating (0-10): ")
            self._storage.update_movie(movie_title_to_update, float(new_movie_rating))
        else:
            print("I'm sorry that movie does not exist in the database.")

    def random_movie_selection(self):
        """This will select a movie at random from the database to suggest to the user to watch."""
        movies = self._storage.list_movies()
        random_movie = random.choice(list(movies.keys()))
        random_rating = movies[random_movie]["Rating"]
        print(f"""Your movie for tonight: {random_movie}, it's rated {random_rating}""")

    def search_movies(self):
        """User is prompted to type in part of the name of a movie they are looking for to see if it's
            in the movie database - this movie is searched for and prints the movie to the console if any matches
            exist in the database"""
        movies = self._storage.list_movies()
        movie_to_search_for = input("Enter part of the movie name: ")
        found_movie = False
        for movie in movies.keys():
            if movie_to_search_for in movie:
                print(f"""{movie}""")
                found_movie = True
        if not found_movie:
            print(f"""I'm sorry, there are no matches for {movie_to_search_for}""")

    def movies_sorted_by_rating(self):
        """This function sorts the movies by rating from highest to lowest and prints them to console"""
        movies = self._storage.list_movies()
        sorted_movies = sorted(list(movies.items()), key=lambda x: x[1]["Rating"], reverse=True)
        for movie in sorted_movies:
            print(f"""{movie[0]}, {movie[1]["Rating"]}""")

    def prints_user_menu(self):
        """Prints the user menu"""
        print(
            "Menu:\n0. Exit \n1. List movies \n2. Add movie \n3. Delete movie \n4. Update movie "
            "\n5. Stats \n6. Random movie \n7. Search movie \n8. Movies Sorted by rating \n9. Create website\n\n")

    def _generate_website(self):
        """Accesses the website generating function from the movies_website_creation file, and confirms to
            the user that the website was created"""
        movies = self._storage.list_movies()
        movies_website_creation.create_website(movies)
        print("Your website was successfully created!\n")

    def run(self):
        """Based on what the user selects from the menu, the functions will be executed"""
        self.prints_user_menu()
        user_selection = input("Enter choice (1-9): ")
        while user_selection != 0:
            if user_selection == "1":
                self._command_list_movies()
            elif user_selection == "2":
                self.add_movie()
            elif user_selection == "3":
                self.delete_movie()
            elif user_selection == "4":
                self.update_movie()
            elif user_selection == "5":
                self._command_movie_stats()
            elif user_selection == "6":
                self.random_movie_selection()
            elif user_selection == "7":
                self.search_movies()
            elif user_selection == "8":
                self.movies_sorted_by_rating()
            elif user_selection == "9":
                self._generate_website()
            else:
                print("Please enter a numer 1-9: ")

            input("Press enter to continue: ")
            self.prints_user_menu()
            user_selection = input("Enter choice (1-9): ")

        self.exit_application()
