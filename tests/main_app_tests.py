from movie_app import MovieApp
from storage_csv import StorageCSV

storage = StorageCSV('data.csv')
movie_app = MovieApp(storage)
movie_app.run()

