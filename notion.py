import requests
from access_token import NOTION_ACCESS_TOKEN

base_url = 'https://api.notion.com/'
DATABASE_ID = 'd9659c3f4e3842ecb4dbcbda20642e20'
PAGE_ID = 'c785add6ba004f379f5eccd0e0668cdc'
tinnitus = {'Title': 'Tinnitus (Wanna be a rock) (돌멩이가 되고 싶어)', 'Artist': ['TOMORROW X TOGETHER'], 'Producer': ['Dystinkt Beats', 'Smash David'], 'Writers': ['Ebby (KOR)', 'Dystinkt Beats', 'Smash David', 'TAEHYUN (TXT)', 'Jeon Jieun (1월 8일)', 'YEONJUN (연준)', '이스란 (Lee Seu Ran)', 'Stella Jang (스텔라장)', '조윤경 (Cho Yoon Kyung)', '\u200bdanke (lalala studio)', '1월8일 (January 8th)', 'DKeyz'], 'Vocals': ['SOOBIN (TXT)', 'YEONJUN (연준)', 'BEOMGYU (TXT)', 'TAEHYUN (TXT)', 'HUENING KAI (TXT)'], 'Phonographic Copyright ℗': ['BIGHIT MUSIC'], 'Copyright  ©': ['BIGHIT MUSIC'], 'Lyricist': ['Ebby (KOR)', 'Dystinkt Beats', 'Smash David', 'TAEHYUN (TXT)', 'Jeon Jieun (1월 8일)', 'YEONJUN (연준)', '이스란 (Lee Seu Ran)', 'Stella Jang (스텔라장)', '조윤경 (Cho Yoon Kyung)', '\u200bdanke (lalala studio)', '1월8일 (January 8th)', 'DKeyz'], 'Composer': ['Ebby (KOR)', 'Dystinkt Beats', 'Smash David', 'TAEHYUN (TXT)', 'Jeon Jieun (1월 8일)', 'YEONJUN (연준)', '이스란 (Lee Seu Ran)', 'Stella Jang (스텔라장)', '조윤경 (Cho Yoon Kyung)', '\u200bdanke (lalala studio)', '1월8일 (January 8th)', 'DKeyz'], 'Label': ['BIGHIT MUSIC']}
cysm = {'Title': '세계가 불타버린 밤, 우린... (Can’t You See Me?)', 'Artist': ['TOMORROW X TOGETHER'], 'Release Date': '2020-05-18', 'Album': 'THE DREAM CHAPTER: ETERNITY', 'Producer': ['“hitman” Bang', 'Slow Rabbit'], 'Writers': ['Eric Zayne', 'Naz Tokio', 'Michel “Lindgren” Schulz', 'Melanie Joy Fontana', 'Supreme Boi', '“hitman” Bang', 'Slow Rabbit'], 'Composer': ['Eric Zayne', 'Naz Tokio', 'Michel “Lindgren” Schulz', 'Melanie Joy Fontana', 'Supreme Boi', '“hitman” Bang', 'Slow Rabbit'], 'Vocals': ['SOOBIN (TXT)', 'YEONJUN (연준)', 'HUENING KAI (TXT)', 'TAEHYUN (TXT)', 'BEOMGYU (TXT)']}

def create_page(song_metadata):
    token = 'Bearer {}'.format(NOTION_ACCESS_TOKEN)
    headers = {'Authorization': token,
               "Notion-Version": "2022-06-28",
               "Content-Type": "application/json"}
    url = _make_url()
    data = _make_data(song_metadata)

    response = None
    try:
        response = requests.post(url, headers = headers, json = data)
        return response.json()

    finally:
        if response is not None:
            response.close()

def _make_data(song_metadata):

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": song_metadata['Title']
                        }
                    }
                ]
            },
            "Artist(s)": {
                "multi_select": _create_people_list(song_metadata['Artist'])
            },
            "Release Date": {
                "date": {
                    "start": song_metadata['Release Date']
                }
            },
            "Album": {
                "select": {
                    "name": song_metadata['Album']
                }
            },
            "Producers": {
                "multi_select": _create_people_list(song_metadata['Producer'])
            },
            "Writers": {
                "multi_select": _create_people_list(song_metadata['Writers'])
            }
        }
    }

    data['properties'] = data['properties'] | _make_other_properties(song_metadata)

    return data

def _make_other_properties(song_metadata):
    all_keys = list(song_metadata.keys())
    of_interest = ['Lyricist', 'Composer', 'Arranger', 'Background Vocals', 'Vocal Arranger',
                   'Keyboards', 'Synthesizer', 'Drums']

    other_properties = dict()

    for key in all_keys:
        if key in of_interest:
            keyword = _make_keyword(key)
            other_properties[keyword] = {
                "multi_select": _create_people_list(song_metadata[key])
            }

    return other_properties

def _make_keyword(key):
    unchanged = ['Keyboards', 'Synthesizer', 'Guitar', 'Vocal Arranger',
                 'Drums']
    if key[-1] != 's' and key not in unchanged:
        return key + 's'
    else:
        return key

def _create_people_list(people: list):
    artist_list = []
    for artist in people:
        artist_list.append({ "name": artist})

    return artist_list
def _make_url(url_type = 'page'):
    if url_type == 'page':
        url = base_url + f'v1/pages'
    else:
        url = base_url

    return url

