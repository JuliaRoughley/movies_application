from movie_app import MovieApp
from storage_JSON import StorageJson
from storage_csv import StorageCSV
from movie_app import MovieApp


def main():
    user_storage = input("Are you using 'JSON' or 'CSV?'")
    if user_storage == "JSON":
        storage = StorageJson('data\\movies.json')
    elif user_storage == "CSV":
        storage = StorageCSV('movies.csv')
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
