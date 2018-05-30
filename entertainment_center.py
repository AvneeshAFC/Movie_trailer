import media			# Imports the module media which constains the class movie. This file contains the movie instancies
# Imports the module fresh_tomatoes which helps in creating our movie
# trailer html page.
import fresh_tomatoes

jobs = media.Movie("Jobs (2013)",
                   "A biopic on the Apple co founder Steve Jobs.",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcSTeTXfbanj4ks4j2l9X1WGsPAF9if5kb1aOAj3AW-2wY5lgHX0",
                   "https://www.youtube.com/watch?v=FrvkCS0ZGPU")  # Creates an instance 'jobs' and passes 4 arguements (movie details)

avatar = media.Movie("Avatar",
                     "A marine on an Alien planet.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


inception = media.Movie("Inception",
                        "A man named Cobb has the power to influence the mind of others by manipulating their dreams.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

fightclub = media.Movie("Fight Club",
                        "An ordinary employee is tired of his drudged existence. His life changes when he meets Tyler, a soap salesman.",
                        "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_ad.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

interstellar = media.Movie("Interstellar",
                           "Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

dictator = media.Movie("The Dictator",
                       "A funny film invloving the dictator, General Alladin",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcSczZQUA0xBAUjgk-aIsB6G-iQYOn6sA4z3dis12puEPFQdGnkd",
                       "https://www.youtube.com/watch?v=cYplvwBvGA4")

movies = [jobs, avatar, inception, fightclub, interstellar,
          dictator]		# A list of instancies (movies)
# The list of movies is passed on this method
fresh_tomatoes.open_movies_page(movies)

# NOTE : THERE WILL BE 11 ERRORS WHEN CHECKING FOR PEP8 REQUIREMENTS OF 'LINE TOO LONG'
# WHICH CAN'T BE AVOIDED AS THE LINKS CAN'T BE BROKEN DOWN.
