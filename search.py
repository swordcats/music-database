import urllib.parse
import requests
from access_token import GENIUS_ACCESS_TOKEN

BASE_GENIUS_URL = 'https://api.genius.com'

def run_search(search_term = None) -> int:

    # STAGE ONE: Get search term
    if search_term is None:
        search_term = _get_search_term()


    # STAGE TWO: Make search request from API and display it to user
    searches = create_search_dict(search_song(search_term))
    print_search_results(searches)

    # STAGE THREE: Have user select the correct song and return the song ID
    result_id = _get_correct_result()
    return searches[result_id][1]

def print_search_results(searches):
    for key in searches:
        print(f"{key}. {searches[key][0]}")
def search_song(search_term):
    url = _build_search_url(search_term)

    response = None

    try:
        response = requests.get(url)
        return response.json()

    finally:
        if response is not None:
            response.close()

def create_search_dict(searches):
    search_results = dict()
    index = 1

    for song in searches['response']['hits']:
        song_title = f"{song['result']['artist_names']} - {song['result']['title']}"
        search_results[index] = (song_title, song['result']['id'])
        index += 1

    return search_results

def _build_search_url(search_term):
    query_parameters = [
        ('q', search_term),
        ('access_token', GENIUS_ACCESS_TOKEN)
    ]

    return f'{BASE_GENIUS_URL}/search?{urllib.parse.urlencode(query_parameters)}'
def _get_search_term():
    return input('Enter search term: ')

def _get_correct_result():
    return int(input('Enter the number of the correct result: '))
