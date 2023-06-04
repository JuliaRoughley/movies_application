from movie_app import MovieApp
from storage_JSON import StorageJson

storage = StorageJson('movies.json')
movie_app = MovieApp(storage)
movie_app.run()