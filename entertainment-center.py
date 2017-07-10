"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link and video trailer link.
    I have used link shortners for poster image link and video
    trailer link because original links were too big."""

    # Deadpool Movie info
    deadpool = media.Movie("Deadpool",
                           """DEADPOOL tells the origin story of former Special
                              Forces operative turned mercenary Wade Wilson""",
                           "https://goo.gl/Nna2uy",
                           "http://y2u.be/gtTfd6tISfw")

    # John Wick Movie info
    john_wick = media.Movie("John Wick",
                            "A retired but deadly hitman seeking vengeance",
                            "https://goo.gl/beMh3P",
                            "http://y2u.be/RllJtOw0USI")

    # Pirates of the Caribbean Movie info
    pirates_of_caribbean = media.Movie("Pirates of the Caribbean",
                                       """Blacksmith Will Turner teams up with
                                          eccentric pirate 'Captain'
                                          Jack Sparrow to save his love.""",
                                       "https://goo.gl/7GWWPj",
                                       "http://y2u.be/naQr0uTrH_s")

    # Spider-Man Movie info
    spider_man = media.Movie("Spider-Man: Homecoming",
                             """Peter Parker tries to balance high school
                                life with being the hero Spider-Man
                                as he faces the Vulture.""",
                             "https://goo.gl/Fn8VGn",
                             "http://y2u.be/n9DwoQ7HWvI")

    # Justice League Movie info
    justice_league = media.Movie("Justice League",
                                 """Batman and Wonder Woman assemble a team
                                    consisting of Flash, Aquaman and Cyborg""",
                                 "https://goo.gl/REurpk",
                                 "http://y2u.be/3cxixDgHUYw")

    # Thor: Ragnarok Movie info
    thor_ragnarok = media.Movie("Thor: Ragnarok",
                                """Thor must defeat the Hulk in a gladiatorial duel
                                   in time to save Asgard from Hela and
                                   the coming Ragnarok.""",
                                "https://goo.gl/Vf4PZ8",
                                "http://y2u.be/v7MGUNV8MxU")

    # A list containing all the names of movie object created.
    movies = [spider_man, justice_league, thor_ragnarok,
              deadpool, john_wick, pirates_of_caribbean]

    """Passing movies list as an argument to the
       open_movie_page() function present in fresh_tomatoes."""
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
