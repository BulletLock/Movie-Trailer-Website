import media
import fresh_tomatoes


#Deadpool Movie info
deadpool = media.Movie("Deadpool",
                       "DEADPOOL tells the origin story of former Special Forces operative turned mercenary Wade Wilson.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")

#John Wick Movie info
john_wick = media.Movie("John Wick",
                        "A retired but deadly hitman seeking vengeance",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=RllJtOw0USI")

#Pirates of the Caribbean Movie info
pirates_of_caribbean = media.Movie("Pirates of the Caribbean",
                                   "Blacksmith Will Turner teams up with eccentric pirate 'Captain' Jack Sparrow to save his love.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
                                   "https://www.youtube.com/watch?v=naQr0uTrH_s")

#Spider-Man Movie info
spider_man = media.Movie("Spider-Man: Homecoming",
                         "Peter Parker tries to balance high school life with being the hero Spider-Man as he faces the Vulture.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

#Justice League Movie info
justice_league = media.Movie("Justice League",
                             "Batman and Wonder Woman assemble a team consisting of Flash, Aquaman, and Cyborg.",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")

#Thor: Ragnarok Movie info
thor_ragnarok = media.Movie("Thor: Ragnarok",
                            "Thor must defeat the Hulk in a gladiatorial duel in time to save Asgard from Hela and the coming Ragnarök.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

movies = [spider_man, justice_league, thor_ragnarok,
          deadpool, john_wick, pirates_of_caribbean]  #A list containing all the names of movie object created.

fresh_tomatoes.open_movies_page(movies)  #Passing movies list as an argument to the open_movie_page() function present in fresh_tomatoes.
