import media
import fresh_tomatoes

#toy_story = media.Movie("Toy Story",
                        #"A story of a boy and his toys that come to life",
                        #"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        #"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

#avatar = media.Movie("Avatar",
                     #"A marine on an alien planet",
                     #"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     #"https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

casablanca = media.Movie("Casablanca",
                         "A love story and daring escape during WWII",
                         "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CasablancaPoster-Gold.jpg/440px-CasablancaPoster-Gold.jpg",
                         "https://www.youtube.com/watch?v=a2MnKebNlRo")
#print (casablanca.storyline)
#casablanca.show_trailer()

who_framed_roger_rabbit = media.Movie("Who Framed Roger Rabbit",
                                     "An innocent cartoon on the run in the real world",
                                     "https://upload.wikimedia.org/wikipedia/en/3/32/Movie_poster_who_framed_roger_rabbit.jpg",
                                     "https://www.youtube.com/watch?v=gpDaNqSXxp0")

trading_places = media.Movie("Trading Places",
                             "Societal role reversals, can they survive?",
                             "https://upload.wikimedia.org/wikipedia/en/4/4d/Trading_Places.jpg",
                             "https://www.youtube.com/watch?v=ZjDbJQKDXCY")


movies = [casablanca, who_framed_roger_rabbit, trading_places]
#fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
print("Class Documentation: " + media.Movie.__doc__)
print ("Class Name: " + media.Movie.__name__)
print ("Class Module: " + media.Movie.__module__)