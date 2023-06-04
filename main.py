from movie_app import MovieApp
from storage_JSON import StorageJson


def main():
    storage = StorageJson('data\\movies.json')
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
