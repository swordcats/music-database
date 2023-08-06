from search import run_search
from credits import retrieve_credits
from notion import create_page
from access_token import GENIUS_ACCESS_TOKEN

def main():
    song_id = run_search()
    credits = retrieve_credits(song_id)

    print(credits)

    for key in credits:
        print(f"{key}: {credits[key]}")

    print(create_page(credits))

if __name__ == '__main__':
    main()