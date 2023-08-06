import urllib.parse
import requests
from access_token import GENIUS_ACCESS_TOKEN
from datetime import date

SUGAR_RUSH_RIDE = 8661639
BASE_GENIUS_URL = 'https://api.genius.com'

def retrieve_credits(song_id):
    song_metadata = search_song(song_id)
    credits = format_credits(song_metadata['response']['song'])

    return credits

def format_credits(song_metadata):
    song = dict()

    song['Title'] = song_metadata['title']
    song['Artist'] = _retrieve_artist_names(song_metadata)
    song['Release Date'] = song_metadata['release_date']
    song['Album'] = song_metadata['album']['name']

    producers = []
    for x in song_metadata['producer_artists']:
        producers.append(x['name'])

    song['Producer'] = producers

    writers = []
    for x in song_metadata['writer_artists']:
        writers.append(x['name'])

    song['Writers'] = writers

    for x in song_metadata['custom_performances']:
        label = x['label']
        credited = []

        for name in x['artists']:
            credited.append(name['name'])

        song[label] = credited

    return song


def search_song(song_id):
    url = _build_song_url(song_id)
    #token = 'Bearer {}'.format(GENIUS_ACCESS_TOKEN)
    #headers = {'Authorization': token}

    response = None

    try:
        response = requests.get(url)
        return response.json()

    finally:
        if response is not None:
            response.close()

def _build_song_url(song_id):
    query_parameters = [
        ('access_token', GENIUS_ACCESS_TOKEN)
    ]

    return f'{BASE_GENIUS_URL}/songs/{song_id}?{urllib.parse.urlencode(query_parameters)}'

def _retrieve_artist_names(song_metadata):
    artists = []

    artists.append(song_metadata['primary_artist']['name'])

    featured = song_metadata['featured_artists']

    if featured:
        for x in featured:
            artists.append(x['name'])

    return artists