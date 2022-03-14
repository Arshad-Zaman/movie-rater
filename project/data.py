# pylint: disable = import-error, invalid-name
""" File to get data """

import os
from random import randrange
from dotenv import find_dotenv, load_dotenv  # type: ignore
import requests  # type: ignore

load_dotenv(find_dotenv())


def get_data():
    """func for getting tmdb data"""
    rand_index = randrange(15)
    MOVIE_BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

    params = {"api_key": TMDB_API_KEY}

    results = requests.get(
        MOVIE_BASE_URL,
        params=params,
    )
    results_json = results.json()

    # results for title, tagline, genres, and a movie poster image url below:
    movie_id = results_json["results"][rand_index]["id"]
    title = results_json["results"][rand_index]["title"]
    overview = results_json["results"][rand_index]["overview"]
    poster_path = results_json["results"][rand_index]["poster_path"]
    img_url = "https://image.tmdb.org/t/p/original"
    img_url += poster_path

    return movie_id, title, overview, img_url
