import imdb
a = imdb.IMDb()
movie_name = input("Enter the name of the movie : ")
movies = a.search_movie((str(movie_name)))
index = movies[0].getID()
movie = a.get_movie(index)
movie_title = movie['title']
movie_year = movie['year']
movie_cast = movie['cast']
list_of_cast = ','.join(map(str, movie_cast))
print("title of the movie is : ", movie_title)
print("year of the release of the movie is : ", movie_year)
print("full cast of the movie is : ",movie_cast)
