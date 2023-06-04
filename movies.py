import statistics
import random
import movie_storage
import requests
import movies_website_creation

def main():
    """ Prints a welcome message and presents a menu of choices to the user, prompting
    them to make a selection, in order to interact with the movie database"""

    print(
        "**********My Movies Database**********\nMenu:\n0. Exit\n1. List movies \n2. Add movie "
        "\n3. Delete movie \n4. Update movie \n5. Stats \n6. Random movie \n7. Search movie \n8."
        " Movies Sorted by rating \n9. Creates website\n\n")
    choice_menu()


def exit_application():
    """Exits the application"""
    print("Bye!")
    exit()


def list_movies():
    """When selected from menu will print the list of all the movies available in the data"""
    movies = movie_storage.list_movies()
    movies_in_total = len(movies)
    print(f"{movies_in_total} movies in total")
    for movie_name, info in movies.items():
        print(f"""{movie_name}: Rated {info["Rating"]}\nYear of release {info["Year"]}""")


def add_movie():
    """Promts the user to enter the title, rating and year of release of the movie they would like to add
    to the database, and then adds that movie data to the database"""
    try:
        movies = movie_storage.list_movies()
        new_movie_name = input("Please enter the name of the movie you would like to add: ")
        if new_movie_name in movies:
            print(f"Movie {new_movie_name} already exists!")
            return
        if movie_storage.add_movie(new_movie_name) == 0:
            print(f"I'm sorry, {new_movie_name} doesn't exist in the database.")
        else:
            movies = movie_storage.add_movie(new_movie_name)
            print(f"Movie {new_movie_name} successfully added")
    except requests.exceptions.RequestException as connection_error:
        print(f"I'm sorry, there has been an error: {connection_error}")


def delete_movie():
    """Prompts user to enter the name of the movie they want to delete, and then deletes that movies
    entire info from the database"""
    movie_title_to_delete = input("Please enter the name of the movie you would like to delete: ")
    movie_storage.delete_movie(movie_title_to_delete)


def update_movie():
    """To update a movies rating, the user is prompted to enter the title, it is searched for and if
    found asks the user for the new rating and then updates the database, otherwise if not found
    tells the user that that movie does not exist in the database."""
    movies = movie_storage.list_movies()
    movie_title_to_update = input("Please enter the name of the movie you wish to update: ")
    if movie_title_to_update in movies:
        new_movie_rating = input("Please enter the new movie rating (0-10): ")
        movie_storage.update_movie(movie_title_to_update, float(new_movie_rating))
    else:
        print("I'm sorry that movie does not exist in the database.")


def get_list_movie_ratings():
    """Creates a list of the ratings of the movies, and is useful to use in other functions"""
    movies = movie_storage.list_movies()
    movie_ratings = []
    for rating in movies.values():
        movie_ratings.append(rating["Rating"])
    return movie_ratings


def movie_statistics():
    """Produces some statistics for the movies in the database, including the average rating, the median rating,
    the best and worst movies."""
    movies = movie_storage.list_movies()
    ratings = get_list_movie_ratings()
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


def random_movie_selection():
    """This will select a movie at random from the database to suggest to the user to watch."""
    movies = movie_storage.list_movies()
    random_movie = random.choice(list(movies.keys()))
    random_rating = movies[random_movie]["Rating"]
    print(f"""Your movie for tonight: {random_movie}, it's rated {random_rating}""")


def search_movies():
    """User is prompted to type in part of the name of a movie they are looking for to see if it's
    in the movie database - this movie is searched for and prints the movie to the console if any matches
    exist in the database"""
    movies = movie_storage.list_movies()
    movie_to_search_for = input("Enter part of the movie name: ")
    found_movie = False
    for movie in movies.keys():
        if movie_to_search_for in movie:
            print(f"""{movie}""")
            found_movie = True
    if not found_movie:
            print(f"""I'm sorry, there are no matches for {movie_to_search_for}""")


def movies_sorted_by_rating():
    """This function sorts the movies by rating from highest to lowest and prints them to console"""
    movies = movie_storage.list_movies()
    sorted_movies = sorted(list(movies.items()), key=lambda x: x[1]["Rating"], reverse=True)
    for movie in sorted_movies:
        print(f"""{movie[0]}, {movie[1]["Rating"]}""")


def prints_user_menu():
    """Prints the user menu"""
    print(
        "Menu:\n0. Exit \n1. List movies \n2. Add movie \n3. Delete movie \n4. Update movie "
        "\n5. Stats \n6. Random movie \n7. Search movie \n8. Movies Sorted by rating \n9. Create website\n\n")


def creates_website():
    """Accesses the website generating function from the movies_website_creation file, and confirms to
    the user that the website was created"""
    movies_website_creation.create_website()
    print("Your website was successfully created!\n")


def choice_menu():
    """Based on what the user selects from the menu, the functions will be executed"""
    prints_user_menu()
    user_selection = input("Enter choice (1-9): ")
    while user_selection != 0:
        if user_selection == "1":
            list_movies()
        elif user_selection == "2":
            add_movie()
        elif user_selection == "3":
            delete_movie()
        elif user_selection == "4":
            update_movie()
        elif user_selection == "5":
            movie_statistics()
        elif user_selection == "6":
            random_movie_selection()
        elif user_selection == "7":
            search_movies()
        elif user_selection == "8":
            movies_sorted_by_rating()
        elif user_selection == "9":
            creates_website()
        else:
            print("Please enter a numer 1-9: ")

        input("Press enter to continue: ")
        prints_user_menu()
        user_selection = input("Enter choice (1-9): ")

    exit_application()


if __name__ == "__main__":
    main()
