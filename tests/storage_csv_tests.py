from storage_csv import StorageCSV

storage = StorageCSV('data.csv')
print(storage.list_movies())
# storage.add_movie(...)