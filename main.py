from search import run_search
from credits import retrieve_credits
from access_token import GENIUS_ACCESS_TOKEN

def main():
    song_id = run_search()
    credits = retrieve_credits(song_id)

    for key in credits:
        print(f"{key}: {credits[key]}")

if __name__ == '__main__':
    while True:
        main()