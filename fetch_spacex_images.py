import requests
import argparse
from secondary_functions import getting_page


def fetch_spacex_launch(launch_id='latest'):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for picture_number, link in enumerate(links):
        getting_page(link, f'spacex{picture_number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Input launch ID')
    parser.add_argument('ID', nargs='?', default='latest')
    launch_id = parser.parse_args().ID
    fetch_spacex_launch(launch_id)
