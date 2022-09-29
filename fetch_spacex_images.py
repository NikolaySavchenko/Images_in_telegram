import requests
import argparse
from secondary_functions import get_image


def fetch_spacex_launch(launch_id='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate(links):
        get_image(link, f'spacex{number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Input launch ID')
    parser.add_argument('ID', nargs='?', default='latest')
    launch_id = parser.parse_args().ID
    fetch_spacex_launch(launch_id)
